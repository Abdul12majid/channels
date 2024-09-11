from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	profile_owner = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='img', blank=True, null=True)
	username = models.CharField(max_length=128, unique=True)
	info = models.TextField(blank=True, null=True)

	def __str__(self):
		return f'{self.profile_owner.username}'

	@property
	def name(self):
		if self.username:
			return self.username
		return self.profile_owner.username