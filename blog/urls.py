from django.urls import path

from .views import index_view, blog_view

app_name = 'blog'

urlpatterns = [
    path('', index_view, name='index'),
    path('blogs/', blog_view, name='blogs')
]