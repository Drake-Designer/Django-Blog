"""Models for About app."""
from django.db import models


class About(models.Model):
    """Simple about section with editable text."""
    body = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "About me"


class CollaborateRequest(models.Model):
    """Stores collaboration requests from visitors."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.name} - {self.email}"
