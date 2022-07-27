from django.urls import path

from apps.users import views

app_name = "users"

urlpatterns = [
    path("", views.SignUpView.as_view(), name="signup"),
]
