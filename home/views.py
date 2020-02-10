from django.shortcuts import render


def index(request):
    """
    A view that displays an Index page
    """
    return render(request, "index.html")