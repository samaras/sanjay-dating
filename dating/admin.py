from django.contrib import admin
from dating import models

# Register your models here.
class ProfileAdminModel(admin.ModelAdmin):
	class Meta:
		models.Profile 


admin.site.register(models.Profile, ProfileAdminModel)
