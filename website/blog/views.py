from django.shortcuts import render
from .models import Post


def home(request):
    """

    :param request:
    :return:
    """
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    """

    :param response:
    :return:
    """
    return render(request, 'blog/about.html', {"title": "About"})