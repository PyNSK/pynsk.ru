from django.contrib import admin

from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost

admin.site.unregister(BlogPost)

custom_fieldset = BlogPostAdmin.fieldsets
custom_fieldset[0][1]["fields"].append('user')


class CustomBlogPostAdmin(BlogPostAdmin):
    # list_editable = BlogPostAdmin.list_editable + ('user',)
    fieldsets = custom_fieldset


admin.site.register(BlogPost, CustomBlogPostAdmin)
