from django.contrib import admin

from articles.models import Article, Category


class CategoryAdmin(admin.ModelAdmin):
    pass


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    list_filter = ['category__title', ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
