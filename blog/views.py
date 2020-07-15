from django.shortcuts import render

from .models import Blog


# index_view
def index_view(request):
    return render(request, 'blog/index.html')


# blog_view
def blog_view(request):
    blogs = Blog.objects.all().order_by('-created')

    context = {'blogs': blogs}
    return render(request, 'blog/blogs.html', context=context)