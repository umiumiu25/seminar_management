# seminars/models.py
import uuid
from django.db import models
from django.contrib.auth.models import User


class Seminar(models.Model):
    id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.id} - {self.title}"


class Application(models.Model):
    id = models.TextField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seminar = models.ForeignKey(Seminar, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=[
            ("pending", "Pending"),
            ("confirmed", "Confirmed"),
            ("canceled", "Canceled"),
        ],
    )

    def __str__(self):
        return f"{self.id} - {self.user} - {self.seminar}"
