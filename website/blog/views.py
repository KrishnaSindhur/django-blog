from django.shortcuts import render


post = [
    {
        "author" : "krishna",
        "title" : "spatans",
        "date" : "january 7, 2019"
    },
    {
        "author": "ninad",
        "title": "pokemon",
        "date": "january 8, 2019"
    }

]

def home(request):
    """

    :param request:
    :return:
    """
    context = {
        'posts': post
    }
    return render(request, 'blog/home.html', context)

def about(request):
    """

    :param response:
    :return:
    """
    return render(request, 'blog/about.html', {"title": "About"})