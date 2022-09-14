from django.views.generic import ListView

from apps.logger_middleware.models import RequestLogger


class ShowAllLogs(ListView):
    model = RequestLogger
    template_name = "logger_middleware/show_all_logs.html"
    context_object_name = "middleware_logs"
