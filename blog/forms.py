"""Forms for the Blog app."""

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """Form for submitting and editing comments on blog posts."""

    class Meta:
        """Meta options for CommentForm."""
        model = Comment
        fields = ("body",)
