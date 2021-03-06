from django.shortcuts import render, get_object_or_404
from .models import post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostListView(ListView):
    model = post
    template_name = "home.html"
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = post
    template_name = "user_posts.html"
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return post.objects.filter(author = user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = post
    template_name = "posts.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = post
    fields=['title', 'content']
    template_name = "post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = post
    fields=['title', 'content']
    template_name = "post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = post
    template_name = "post_delete.html"

    success_url = "/"
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def home(request):
    context = {
        'posts':post.objects.all()
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {'title': "About"})