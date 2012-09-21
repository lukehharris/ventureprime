from django.contrib import admin
from ventureprime.emailcollection.models import VPUser

class VPUserAdmin(admin.ModelAdmin):
    list_display = ('date','user_type','email','name')
    search_fields = ('date','user_type','email','name')
    list_filter = ('date',)
    date_hierarchy = 'date'

admin.site.register(VPUser, VPUserAdmin)