from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, EditForm

# Create your views here.

# def home(request):
#    return render(request, 'home.html', {})

# We'll use class based views from now

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class DetailedView(DetailView):
    model = Post
    template_name = 'detail.html'

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    #fields = '__all__' not needed as we are using PostForm
    #fields = ('title','author','body') if you want to pass them seperately

class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update.html'
    #fields = ('title', 'body')
