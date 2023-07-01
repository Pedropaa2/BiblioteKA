from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class Borrow(models.Model):
    borrow_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(default=return_date)
    is_delay = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_retuned = models.BooleanField(default=True)
    blocking_end_date = models.DateTimeField(null=True, blank=True)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="borrow"
    )

    copy = models.ForeignKey(
        "copy.copy",
        on_delete=models.PROTECT,
        related_name="copy"
    )

    def save(self, *args, **kwargs):
        if not self.return_date:
            self.return_date = self.borrow_date + timedelta(
                days=3
                )
            if self.return_date.weekday() in [5, 6]:
                self.return_date += timedelta(
                    days=3 - self.return_date.weekday()
                    )

            if self.return_date and self.return_date < timezone.now():
                self.is_delay = True
                self.is_active = False
                self.blocking_end_date = timezone.now() + timedelta(days=7)

        if self.is_returned:
            self.is_active = False
            self.blocking_end_date = timezone.now() + timedelta(days=7)

        super().save(*args, **kwargs)

        self.user.update_blocked_status()


@receiver(post_save, sender=Borrow)
def update_user_blocked_status(sender, instance, **kwargs):
    instance.update_blocked_status()

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
