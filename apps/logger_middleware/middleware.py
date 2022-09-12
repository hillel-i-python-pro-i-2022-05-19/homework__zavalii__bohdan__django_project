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
        # log_path = request.path
        # user_is_auth = request.user.is_authenticated
        # username = request.user
        # time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # request_method = request.method
        message = f"[{self._NAME}] ~ {request.path} ~ {request.user.is_authenticated} ~ " \
                  f"{request.user} ~ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        self.logger.info(f"[before] {message}")

        # Get resp
        response = self.get_response(request)
        create_log = RequestLogger.objects.create(
            username=request.user,
            log_path=request.path,
            user_is_auth=request.user.is_authenticated,
            method=request.method
        )
        for request.user in RequestLogger.objects.all():
            if request.user == RequestLogger.username and \
                request.path == RequestLogger.log_path:
                obj, created = RequestLogger.objects.update_or_create(
                    username=request.user,
                    log_path=request.path,
                    defaults={"latest_entry": f"{datetime.now()}"},
                )
        # Code to be executed for each request/response after the view is called.
        self.logger.info(f"[after] {message}")

        return response
