from django.urls import path, include
#from . import views
from .views import HomeView, DetailedView, AddPost, UpdatePost, DeletePost, AddCategory

urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', DetailedView.as_view(), name='article'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('add_category/', AddCategory.as_view(), name='add_category'),
    path('article/update/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('article/del/<int:pk>', DeletePost.as_view(), name='delete_post'),
]
