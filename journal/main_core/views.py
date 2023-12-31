from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """The entry point for the website."""
    context = {}
    return render(request, "main_core/index.html", context)
