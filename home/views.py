from django.shortcuts import render


def index(request):
    """A view to return the index page"""

    return render(request, "home/index.html")


def contact(request):

    return render(request, "home/contact.html")
