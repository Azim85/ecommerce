from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import View
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PostForm
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict

class IndexView(View):
    def get(self, request):
        posts = Post.objects.order_by('-published')
        return render(request, 'main/index.html', {'posts':posts})
    
class CreatePostView(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'main/create.html', context={'form':form})    
    
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return HttpResponse('post created')
  