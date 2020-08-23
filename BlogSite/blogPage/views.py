from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.

# def home(request):
#    return render(request, 'home.html', {})

# We'll use class based views from now

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    #ordering = ['-id']  #hacky way of doing this
    ordering = ['-post_date']

class DetailedView(DetailView):
    model = Post
    template_name = 'detail.html'

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    #fields = '__all__' not needed as we are using PostForm
    #fields = ('title','author','body') if you want to pass them seperately

class AddCategory(CreateView):
    model = Category
    #form_class = PostForm
    fields = '__all__'
    template_name = 'category.html'

class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update.html'
    #fields = ('title', 'body')

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
