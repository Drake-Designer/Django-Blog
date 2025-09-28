"""Admin configuration for the Blog app."""

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin  # third-party
from .models import Post, Comment  # local


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """Admin interface for Post model with Summernote integration."""
    list_display = ("title", "slug", "status", "created_on")
    search_fields = ["title", "content"]
    list_filter = ("status", "created_on")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin interface for Comment model."""
    list_display = ("author", "post", "approved", "created_on")
    list_filter = ("approved", "created_on")
    search_fields = ("author__username", "message")
