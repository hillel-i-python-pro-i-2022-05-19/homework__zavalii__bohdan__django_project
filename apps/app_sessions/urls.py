from django.urls import path

from apps.app_sessions import views

app_name = "app_sessions"

urlpatterns = [
    path("", views.SessionView.as_view(), name="index"),
]
