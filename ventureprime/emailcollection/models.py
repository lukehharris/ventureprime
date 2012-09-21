from django.db import models

class VPUser(models.Model):
	name = models.CharField(blank=True,max_length=100)
	email = models.EmailField(max_length=100)
	date = models.DateTimeField()
	user_type = models.CharField(max_length=20)

	def __unicode__(self):
		return u'%s, %s, %s, %s' % (self.email, self.name, self.user_type, self.date)

	class Meta:
		ordering = ['date']