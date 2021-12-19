from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment



@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'approved', 'created_on')    
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email_address', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
