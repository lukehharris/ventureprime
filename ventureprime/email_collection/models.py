from django.db import models

class User(models.Model):
	date_added = models.DateField()
	email = models.EmailField(max_length=100)
	name = models.CharField(max_length=30, blank=True)
	#Takes values 'Venture', 'Primer', or 'Both'
	user_type = models.CharField(max_length=30)

	def __unicode__(self):
		return u'%s, %s, %s, %s' % (self.name, self.email, self.user_type, self.date_added)

	class Meta:
		ordering = ['date_added']
