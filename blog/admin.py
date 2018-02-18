from django.contrib import admin
from .models import Post, Comment


def ApproveSelected(modeladmin, request, queryset):
    for element in queryset:
        element.approved = True
        element.save()


ApproveSelected.short_description = "Approve selected comments"


class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'text', 'date', 'approved']
    actions = [ApproveSelected]


admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)
