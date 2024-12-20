# render is how we render the static html files
from django.shortcuts import render

# TemplateView is a class-based view that renders the profile template
from django.views.generic import TemplateView

from django.http import HttpResponse, HttpRequest


def index(request):
    print(request.user)
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def resume(request):
    return render(request, "resume.html")

def projects(request):
    return render(request, "projects.html")

def photos(request):
    return render(request, "photos.html")

def health_check(request):
    return HttpResponse("OK", status=200)