from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from django.views.generic import TemplateView


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    
    def get(self, request):
        return render(request, 'registration/register.html')

    def post(self, request, *args, **kwargs):
        # Handle both API and form submissions
        if request.content_type == 'application/json':
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                login(request, user)
                return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Handle form submission
            username = request.POST.get('username')
            email = request.POST.get('email', '')
            password = request.POST.get('password1') or request.POST.get('password')
            
            if not all([username, password]):
                return render(request, 'registration/register.html', 
                            {'error': 'Username and password are required'})

            try:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                login(request, user)
                return redirect('/')
            except Exception as e:
                return render(request, 'registration/register.html', 
                            {'error': str(e)})


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_msg = "Invalid credentials. Please try again."
            if not User.objects.filter(username=username).exists():
                error_msg = "Username not found."
            return render(request, 'registration/login.html', {'error': error_msg})
    
    return render(request, 'registration/login.html')


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        user = serializer.validated_data
        login(request, user)
        return Response(UserSerializer(user).data)

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

    def get(self, request):
        logout(request)
        return redirect('/')

class UserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class HomeView(TemplateView):
    template_name = 'home.html'


# from django.http import HttpResponse
# from django.views import View

# class SimpleHomeView(View):
#     def get(self, request):
#         return HttpResponse("Welcome to Chess Tactics Trainer")