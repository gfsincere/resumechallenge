# TemplateView is a class-based view that renders the profile template
from django.views.generic import TemplateView

# LoginRequiredMixin is a mixin that requires the user to be logged in to access the profile page
from django.contrib.auth.mixins import LoginRequiredMixin




# LoginRequiredMixin is a mixin that requires the user to be logged in to access the profile page for the ProfileView class
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
