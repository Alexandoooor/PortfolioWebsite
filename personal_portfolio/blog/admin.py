from django.contrib import admin
from blog.models import Post, Category, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'post')

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
