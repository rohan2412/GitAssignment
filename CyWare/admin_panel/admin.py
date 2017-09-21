from django.contrib import admin
from models import User

class AuthorAdmin(admin.ModelAdmin):
    fields = ('login', 'created_dt', 'git_id', 'avatar_url', 'url', 'html_url', 'score', 'updated_dt')
    readonly_fields = fields
    list_display = fields
    search_fields = ('login',)
    list_display_links = ('login', 'git_id')
    list_filter = ('created_dt', 'updated_dt')

admin.site.register(User, AuthorAdmin)
