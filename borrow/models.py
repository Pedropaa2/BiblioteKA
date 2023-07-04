from django.db import models
from django.utils import datetime_safe


class Borrow(models.Model):
    borrow_date = models.DateTimeField(default=datetime_safe.datetime.now)
    return_date = models.DateTimeField(default=datetime_safe.datetime.now)
    is_delay = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_returned = models.BooleanField(default=False)
    blocking_end_date = models.DateTimeField(null=True, blank=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user"
    )

    copy = models.ForeignKey(
        "app_copy.Copy", on_delete=models.PROTECT, related_name="copy"
    )
