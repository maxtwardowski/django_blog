from django.contrib import admin
from .models import Post, Comment


def ApproveSelected(modeladmin, request, queryset):
    queryset.update(status='p')
    queryset.approved_comment = True
    queryset.save()


ApproveSelected.short_description = "Approve comments"


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'text']
    actions = [ApproveSelected]


admin.site.register(Post)
admin.site.register(Comment)
