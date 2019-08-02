from django.contrib import admin
from apps.blog.models import *

# Register your models here.


class SourceAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['id', 'name', 'url']


class CategoryAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['id', 'name', 'slug']
    readonly_fields = ('slug',)


class NodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'category', 'num_topics', 'show_status']
    list_display_links = ['id', 'name', 'slug', 'category', 'num_topics']
    list_editable = ["show_status", ]
    readonly_fields = ('slug',)


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_display_links = ['id', 'name', 'slug']
    readonly_fields = ('slug',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'node', 'num_views', 'show_status', 'slug', 'user']
    list_display_links = ['id', 'title', 'node', 'num_views', 'user']
    search_fields = ['title_short', 'user', 'content']
    list_editable = ["show_status", ]
    # style_fields = {"content": "ueditor"}
    readonly_fields = ('slug',)
    show_detail_fields = ['show_status', ]


class FriendsURLAdmin(admin.ModelAdmin):
    list_display = ['id', 'friend_name', 'site_name', 'show_status', 'site_link']
    list_display_links = ['id', 'friend_name', 'site_name', 'site_link']
    list_editable = ["show_status", ]

    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Node, NodeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(FriendsURL, FriendsURLAdmin)
