from django.urls import path

from .views import index_view, blog_view, user_blog

app_name = 'blog'

urlpatterns = [
    path('', index_view, name='index'),
    path('blogs/', blog_view, name='blogs'),
    path('user/<int:pk>/', user_blog, name='user_blog')
]