from django.contrib import admin
from .models import Category, News

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'region', 'created_at', 'is_top', 'views')
    list_filter = ('category', 'region', 'is_top')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_top',)