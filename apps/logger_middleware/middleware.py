import logging
from datetime import datetime

from collections.abc import Callable
from typing import ClassVar
from apps.logger_middleware.models import RequestLogger


class LoggingMiddleware:
    _NAME: ClassVar[str] = "HTTP Logger"

    def __init__(self, get_response: Callable):
        """One-time configuration and initialization."""
        self.get_response = get_response
        self.logger = logging.getLogger("django")
        self.logger.info(f"Init {self._NAME}")

    def __call__(self, request):
        # Code to be executed for each request before the view (and later middleware) are called.

        message = f"[{self._NAME}] ~ {request.path} ~ {request.user.is_authenticated} ~ " \
                  f"{request.user} ~ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        self.logger.info(f"[before] {message}")

        # Get resp
        response = self.get_response(request)

        counter = 1
        all_logs = RequestLogger.objects.all()

        for log in all_logs.reverse():
            if not RequestLogger.objects.filter(
                username=request.user, log_path=request.path).exists():
                RequestLogger.objects.create(
                    username=request.user,
                    log_path=request.path,
                    user_is_auth=request.user.is_authenticated,
                    method=request.method,
                    counter=counter
                )
            else:
                log.delete()
            log.save()

        # Code to be executed for each request/response after the view is called.
        self.logger.info(f"[after] {message}")

        return response
