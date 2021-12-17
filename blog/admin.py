from django.contrib import admin
from blog.models import Post, Tag, Comment


class AdminPost(admin.ModelAdmin):
    raw_id_fields = ['author', 'tags', 'likes']


class AdminComment(admin.ModelAdmin):
    raw_id_fields = ['author', 'post']


admin.site.register(Post, AdminPost)
admin.site.register(Tag)
admin.site.register(Comment, AdminComment)
