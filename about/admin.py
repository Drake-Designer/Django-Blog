from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class AboutAdmin(SummernoteModelAdmin):
    list_display = ('title', 'updated_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)
