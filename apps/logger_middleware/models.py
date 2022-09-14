from django.db import models


class RequestLogger(models.Model):
    username = models.CharField(
        "User's name", max_length=200,
    )
    log_path = models.CharField(
        "Path to the log data",
        max_length=1000,
    )
    user_is_auth = models.CharField(
        "Shows whether the user is authenticated or not",
        max_length=200,
    )
    method = models.CharField(
        "HTTP Method",
        max_length=20,
    )
    counter = models.PositiveIntegerField(
        "Counter",
        default=1,
    )
    latest_entry = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.pk} ~ {self.username} ~ {self.log_path} ~ {self.latest_entry}"

    __repr__ = __str__
