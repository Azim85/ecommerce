from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class IndexView(ListView):
    """ Shows two recent posts per page created by users """
    template_name = 'main/index.html'
    model = Post
    context_object_name = 'posts'
    ordering = ['-published']
    paginate_by = 2
    
class UserPostsView(ListView):
    """ Shows two recent posts per page created by current users """
    template_name = 'main/posts.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 2    
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-published')
    
class PostCreateView(LoginRequiredMixin, CreateView):
    """ Creates new post """
    model = Post
    fields = ['title', 'content']
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Updates current post """
    model = Post
    fields = ['title', 'content']
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostUpdateView, self).form_valid(form)    
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
    
class PostDetailView(DetailView):
    """ Shows current post in detail """
    model = Post    
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Removes current post """
    model = Post        
    success_url = reverse_lazy('main:index')
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

      