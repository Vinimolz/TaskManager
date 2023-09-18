from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import User

class AppUser(AbstractUser):
    bio = models.TextField(max_length=500, default="")

    POSITION_CHOICES = [
        ('Manager', 'Manager'),
        ('QA', 'QA'),
        ('Developer', 'Developer')
    ]

    position = models.CharField(max_length=10, choices=POSITION_CHOICES, blank=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        related_name="appusers",  # Custom related name
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="appusers",  # Custom related name
    )

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()
    assigned_to = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='tasks')
