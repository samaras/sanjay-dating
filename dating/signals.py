from django.conf import settings
from django.db.models.signals import post_save
from dating.models import Profile
from django.dispatch import receiver 

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_handler(sender, instance, created, **kwargs):
	if not created:
		return
	# Create profile object
	profile = Profile(user=instance)
	profile.save()
