from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    verified = models.BooleanField(default=False)
    
    USERTYPE_CHOICES = (
        ('V', 'Venture'),
        ('P', 'Primer'),
    )
    usertype = models.CharField(max_length=1, choices=USERTYPE_CHOICES)

#if a new user account is created, make a profile for them as well
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
    	UserProfile.objects.create(user=instance)