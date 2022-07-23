from django.contrib import admin
from .models import Bb, Category


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'category')
    list_display_links = ('title', 'content', 'price', 'published', 'category')
    list_filter = ('title', 'category')
    search_fields = ('title', 'content')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Bb, BbAdmin)
admin.site.register(Category, CategoryAdmin)




