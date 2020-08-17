from django.urls import path, include
#from . import views
from .views import HomeView, DetailedView, AddPost, UpdatePost

urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', DetailedView.as_view(), name='article'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('article/update/<int:pk>', UpdatePost.as_view(), name='update_post'),
]
