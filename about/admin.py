"""Admin for About app."""
from django.contrib import admin
from .models import About, CollaborateRequest


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """Admin for About model."""
    list_display = ("id", "updated_on")


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """Admin for CollaborateRequest model."""
    list_display = ("name", "email", "read", "created_on")
    list_filter = ("read", "created_on")
    search_fields = ("name", "email", "message")
