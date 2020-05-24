from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class MyUser(AbstractUser):
    display_name = models.CharField(max_length=50, null=True, blank=True)


class WorkTicket(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
        ('Invalid', 'Invalid')
    ]
    title = models.CharField(max_length=100)
    time_filed = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    creator = models.ForeignKey(
        MyUser,
        on_delete=models.SET('User has been deleted'),
        related_name='created_by'
        )
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default='New')
    assigned_to = models.ForeignKey(
        MyUser,
        on_delete=models.SET('User has been deleted'),
        related_name='assigned_to'
        )
    completed_by = models.ForeignKey(
        MyUser,
        on_delete=models.SET('User has been deleted'),
        related_name='completed_by'
        )

    def __str__(self):
        return self.title
