from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _ 

import datetime
from django.utils.timezone import utc

GENDER_TYPE = (
	('M', 'Male'),
	('F', 'Female'),
	# ('C', 'Couple')
)


class Profile(models.Model):
	# Relations
	user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile", verbose_name=_("user"),)
	# Attributes
	profile_pic = models.ImageField(upload_to='/avatars')
	gender = models.CharField(max_length=1, choices=GENDER_TYPE)
	licence_number = models.CharField(max_length=45)
	sn_number = models.CharField(max_length=60)
	more_about_myself = models.TextField(blank=True, null=True)
	what_i_like = models.CharField(max_length=200, blank=True, null=True)
	created_on = models.DateTimeField("Created on", auto_now_add=True)
	updated_on = models.DateTimeField("Updated on", auto_now=True)

	# Functions
	def __unicode__(self):
		return _("Profile %s") % ' '.join([
			self.user.first_name, 
			self.last_name
		])

	# Meta
	class Meta:
		verbose_name = _("Profile")
		verbose_name_plural = _("Profiles")
		ordering = ['-id']

class Dating(models.Model):
	guy_looking = models.ForeignKey(User, verbose_name=_("Guy looking"), related_name="user_guy_looking")
	girl_looking = models.ForeignKey(User, verbose_name=_("Girl looking"), related_name="user_girl_looking")

	class Meta:
		verbose_name = _("Dating")

class Choice(models.Model):
	choice = models.CharField(max_length=45)
	user = models.ForeignKey(User, related_name="user_choice")

class Question(models.Model):
	question = models.CharField(max_length=150)

	class Meta:
		verbose_name = _("Question")
		verbose_name_plural = _("Questions")

class Answer(models.Model):
	user = models.ForeignKey(User, related_name="user_answer")
	question = models.ForeignKey(Question)
	answer = models.CharField(max_length=200)
	created_on = models.DateTimeField("Created on", auto_now_add=True)
	updated_on = models.DateTimeField("Updated on", auto_now=True)

	class Meta:
		verbose_name = _("Answer")
		verbose_name_plural = _("Answers")

class UsersDating(models.Model):
	user = models.ForeignKey(User, related_name="user_dating")
	date_of_date = models.DateTimeField()
	feedback = models.TextField(blank=True, null=True)
	confirmed = models.BooleanField(default=False)
	bg_check_summary = models.TextField()
	bg_check_status = models.CharField(max_length=45)

	class Meta:
		verbose_name = _("Users Dating")
		verbose_name_plural = _("Users Dating")

class CreditCardCharges(models.Model):
	user = models.ForeignKey(User)
	address_line1 = models.CharField(max_length=100)
	address_line2 = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	address_zip = models.CharField(max_length=20)
	address_state = models.CharField(max_length=60)
	stripe_id = models.CharField(max_length=30)
	added_at = models.DateTimeField(auto_now_add=datetime.datetime.now)

