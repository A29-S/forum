from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	image = models.ImageField(default = 'default_image.png', upload_to = 'profile_picture')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kawrgs):
		super().save(*args, **kawrgs)

		img = Image.open(self.image.path)

		if img.height > 400 or img.width > 400:
			resize_image = (400 , 400)
			img.thumbnail(resize_image)
			img.save(self.image.path)
