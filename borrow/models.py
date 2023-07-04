from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Borrow(models.Model):
    borrow_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(default=timezone.now)
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

#  Pedro aqui estara chamando a função para fazer o updated do is_blocked
# na tabela do usuario
#       a função precisa ser algo assim:

#     def update_blocked_status(self): (possivel nome da função)
#         active_borrow_books = self.borrowbook_set.filter(is_active=True)

#         if active_borrow_books.exists():
#             self.is_blocked = False
#         else:
#             self.is_blocked = True

#         self.save()
