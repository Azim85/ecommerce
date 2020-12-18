from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from .forms import RegisterForm, LoginForm, ProfileForm, ProfileImageForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib import  messages
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterView(View):
    """ Registration with default user profile picture """
    def get(self, request):
        form = RegisterForm()
        context = {'form':form}
        return render(request, 'users/register.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            create_profile = Profile(image='default.png', profile_id=user.id)
            create_profile.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can log in now')
            return redirect('login')
        else:
            return redirect('register')
        
class LoginView(View):
    """ Login check view """
    def get(self, request):
        form = LoginForm
        context = {'form':form}
        if request.user.is_authenticated:
            return redirect('main:index')
        return render(request, 'users/login.html', context) 
    
    def post(self,request):
        form = LoginForm(request.POST)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        login(request, user)
        return redirect('main:index')
    
class LogoutView(LoginRequiredMixin, View):
    """ Logout """
    def get(self,request):
        user = request.user.username
        logout(request)
        messages.success(request, f'{user} you have successfully logged out! Thank you for visiting!')
        return redirect('main:index')    
    
class ProfileUpdateView(LoginRequiredMixin, View):
    """ Updates user profile information """
    
    def get(self, request, pk):
        form_u = ProfileForm(instance=request.user)
        form_p = ProfileImageForm(instance=request.user.profile)
        return render(request, 'users/profile_form.html', {'form_u':form_u, 'form_p':form_p, 'id':pk})
    
    def post(self, request, pk):
        form_u = ProfileForm(request.POST, instance=request.user)
        form_p = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        
        if form_u.is_valid() and form_p.is_valid():
            new_user = form_u.save(commit=False)
            new_user.user = request.user
            new_user.save()
            form_p.save()
            return render(request, 'users/profile_form.html', {'form_u':form_u, 'form_p':form_p, 'id':pk})
        
        
        