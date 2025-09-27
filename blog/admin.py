from django.contrib import admin
from .models import Post, Comment, CollaborateRequest, About
from django_summernote.admin import SummernoteModelAdmin

# Customising the Post template in the admin panel


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


admin.site.register(Comment)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("id", "updated_on")


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "read", "created_on")
    list_filter = ("read", "created_on")
    search_fields = ("name", "email", "message")
