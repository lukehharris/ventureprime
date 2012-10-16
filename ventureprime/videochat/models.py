from django.db import models

class SessionId(models.Model):
	sessionId = models.CharField(max_length=100)
	sessionUrlEnding = models.CharField(max_length=100)
