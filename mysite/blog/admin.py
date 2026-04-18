from django.contrib import admin

from.models import post
class postAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_published')

admin.site.register(post, postAdmin)