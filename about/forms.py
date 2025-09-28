"""Forms for About app."""
from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """Form users fill to request collaboration."""
    class Meta:
        model = CollaborateRequest
        fields = ("name", "email", "message")
