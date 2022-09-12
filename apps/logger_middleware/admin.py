from django.contrib import admin

from apps.logger_middleware.models import RequestLogger


class LoggerAdmin(admin.ModelAdmin):
    list_display = ("username", "method", "log_path", "user_is_auth", "latest_entry")


admin.site.register(RequestLogger, LoggerAdmin)
