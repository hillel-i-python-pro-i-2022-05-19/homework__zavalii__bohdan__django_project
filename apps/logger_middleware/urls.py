from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.logger_middleware.views import ShowAllLogs

app_name = "middleware_logs"

urlpatterns = [
    path("", login_required(ShowAllLogs.as_view()), name="show_all_logs"),
]
