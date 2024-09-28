# render is how we render the static html files
from django.shortcuts import render
# TemplateView is a class-based view that renders the profile template
from django.views.generic import TemplateView
# LoginRequiredMixin is a mixin that requires the user to be logged in to access the profile page
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    print(request.user)
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def resume(request):
    return render(request, 'resume.html')

# LoginRequiredMixin is a mixin that requires the user to be logged in to access the profile page for the ProfileView class
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'