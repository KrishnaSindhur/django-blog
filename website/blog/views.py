from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """

    :param request:
    :return:
    """
    return HttpResponse('<h1> my blog home</h1>')

def about(response):
    """

    :param response:
    :return:
    """
    return HttpResponse('<h1> my blog about </h1>')