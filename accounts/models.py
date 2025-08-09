from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models
from django.conf import settings

class User(AbstractUser):
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    reputation = models.IntegerField(default=0)

    def __str__(self):
        return self.username
    def get_badge(self):
        if self.reputation >= 1000:
            return "gold"
        elif self.reputation >= 500:
            return "silver"
        elif self.reputation >= 100:
            return "bronze"
        return None


class Badge(models.Model):
    BADGE_CHOICES = [
        ('gold', 'Gold'),
        ('silver', 'Silver'),
        ('bronze', 'Bronze'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='badges')
    badge_type = models.CharField(max_length=10, choices=BADGE_CHOICES)
    reason = models.CharField(max_length=255)
    awarded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_badge_type_display()} - {self.user.username}"
