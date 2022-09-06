from django.db import models
from apps.logger.middleware import LoggingMiddleware

class RequestLogger(models.Model):
    ...
