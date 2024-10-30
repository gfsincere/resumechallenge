from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

app_name = "public"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("resume", views.resume, name="resume"),
    path("projects", views.projects, name="projects"),
    path("photos", views.photos, name="photos"),
    path("health/", views.health_check, name="health_check"),
]
