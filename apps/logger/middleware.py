import logging
from datetime import datetime

from django.utils import timezone
from collections.abc import Callable
from typing import ClassVar
from apps.contacts.models import Contact


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

        # Code to be executed for each request/response after the view is called.
        self.logger.info(f"[after] {message}")

        return response

