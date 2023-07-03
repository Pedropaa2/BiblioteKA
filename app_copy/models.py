from django.db import models


class ExpectedChoice(models.TextChoices):
    BAD = "Bad"
    GOOD = "Good"
    VERY_GOOD = "Very Good"


class Copy(models.Model):
    book = models.ForeignKey(
        "book.Book", on_delete=models.CASCADE, related_name="copies"
    )
    condition = models.CharField(max_length=20, choices=ExpectedChoice.choices)
    paperback = models.IntegerField()
    quantity = models.IntegerField()
    reviews = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return f"Copy {self.pk} - {self.book.title}"
