from django.contrib import admin
from .models import HeadNews, News, Category,Comments,NewUser


# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'is_published')
    search_fields = ('name', 'text')
    list_display_links = ('id', 'name')
    list_filter = ('is_published', 'date')
    prepopulated_fields = {'slug': ('name',)}


class HeadNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date','is_published')
    search_fields = ('name', 'text')
    list_display_links = ('id', 'name')
    list_filter = ('is_published', 'date')
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'id')
    list_display_links = ('id', 'name')


admin.site.register(Comments)
admin.site.register(HeadNews, HeadNewsAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(NewUser)


