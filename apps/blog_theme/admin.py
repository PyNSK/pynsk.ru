from copy import deepcopy

from django.contrib import admin
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost
from mezzanine.generic.models import Keyword

admin.site.unregister(BlogPost)

custom_fieldset = deepcopy(BlogPostAdmin.fieldsets)
custom_fieldset[0][1]["fields"].insert(-2, 'user')


class CustomBlogPostAdmin(BlogPostAdmin):
    # list_editable = BlogPostAdmin.list_editable + ('user',)
    fieldsets = custom_fieldset


class KeywordAdmin(admin.ModelAdmin):
    search_fields = ('slug', 'title')


admin.site.register(BlogPost, CustomBlogPostAdmin)
admin.site.register(Keyword, KeywordAdmin)
