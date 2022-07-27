from django.contrib.auth.decorators import login_required
from django.urls import path, include

from apps.contacts import views

app_name = "contacts"

urlpatterns = [
    path("", login_required(views.ShowAllContactsView.as_view()), name="show_all"),
    path("create", login_required(views.ContactCreateView.as_view()), name="create"),
    path(
        "<int:pk>/",
        include(
            [
                path("edit", login_required(views.ContactUpdateView.as_view()), name="edit"),
                path("delete", login_required(views.DeleteContactsView.as_view()), name="delete"),
            ]
        ),
    ),
]
