from django.contrib import admin
from ventureprime.email_collection.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('date_added','user_type','email','name')
    search_fields = ('date_added','user_type','email','name')
    list_filter = ('date_added',)
    date_hierarchy = 'date_added'

admin.site.register(User, UserAdmin)