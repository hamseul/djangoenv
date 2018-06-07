from django.contrib import admin
from post.models import Category, Post, Comment
from post.forms import MyPostAdminForm

from django.contrib.admin import AdminSite
class CommentAdminSite(AdminSite):
    site_header = 'Comment administration'
comment_admin = CommentAdminSite(name='comment admin')
comment_admin.register(Comment)

class PostAdmin(admin.ModelAdmin):
    form = MyPostAdminForm
    list_per_page = 10
    list_display = (
        'id', 'title', 'member',
        'is_deleted', 'created_at', )
    list_editable = ('is_deleted', )
    list_filter = ( 'member__permission', 'category__name', 'is_deleted', )

    fieldsets = (
        ('기본정보', {
            'fields': (('member', 'category', ), )
        }),
        ('제목및내용', {
            'fields': (
                'title', 'subtitle', 'content',
            )
        }),
        ('삭제', {
            'fields': ('is_deleted', 'deleted_at', )
        })
    )

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
