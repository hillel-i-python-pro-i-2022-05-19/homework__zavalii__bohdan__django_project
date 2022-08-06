from django.urls import reverse_lazy
from django.views import generic

from apps.users.forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    template_name = "users/signup.html"
    success_url = reverse_lazy("login")
    form_class = CustomUserCreationForm
