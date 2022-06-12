from django.urls import path

from user_generator.views import generate_users_view

urlpatterns = [
    path('', generate_users_view),
    path('<int:users_count>', generate_users_view)
]
