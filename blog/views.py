from django.shortcuts import render

from .models import Blog, User


# index_view
def index_view(request):
    return render(request, 'blog/index.html')


# blog_view
def blog_view(request):
    blogs = Blog.objects.all().order_by('-created')

    context = {'blogs': blogs}
    return render(request, 'blog/blogs.html', context=context)


def user_blog(request, pk):
    user_blog = Blog.objects.filter(user_id=pk)
    user_name = User.objects.filter(id=pk).first()

    context = {
        'user_blog': user_blog,
        'user_name': user_name
    }
    return render(request, 'blog/user_blog.html', context)