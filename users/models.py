from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Creator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name = "First Name", max_length=50)
    last_name = models.CharField(verbose_name = "Last Name", max_length=50)
    gmail_email = models.EmailField(verbose_name = "Google Email", max_length=254, unique = True, null = True)
    image = models.ImageField(upload_to="media/user_pics", default="default_user.png")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height>400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)

# Create your models here.
