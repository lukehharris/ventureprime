from django.contrib import admin
from ventureprime.videochat.models import SessionId

class SessionIdAdmin(admin.ModelAdmin):
	list_display = ('sessionId','sessionUrlEnding')
	search_fields = ('sessionId','sessionUrlEnding')

admin.site.register(SessionId, SessionIdAdmin)