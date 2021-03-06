from django.db import models
from users.models import Creator
from PIL import Image

class Event(models.Model):
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    title = models.CharField(verbose_name = "Event Name", max_length=50)
    description = models.TextField(verbose_name = "Event Description", max_length=400)
    created_on = models.DateField(auto_now=True)
    date = models.DateField(verbose_name = "Event Date", auto_now=False)
    time = models.TimeField(verbose_name = "Event Time", auto_now=False)
    
    poster = models.ImageField(upload_to="posters", default="default_poster.png")
    url = models.CharField(max_length=50)

    registrations = models.IntegerField(default = 0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.poster.path)

        if img.height>800 or img.width > 1000:
            output_size = (800, 1000)
            img.thumbnail(output_size)
            img.save(self.poster.path)

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(verbose_name = "Participant Name", max_length=50)
    phone = models.CharField(verbose_name = "Participant Mobile", max_length=14)
    email = models.EmailField(verbose_name = "Participant Email", max_length=100)
    college = models.CharField(verbose_name = "Participant College", max_length=100)
    image = models.ImageField(upload_to="participants", default="default_user.png")
    date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height>800 or img.width > 1000:
            output_size = (800, 1000)
            img.thumbnail(output_size)
            img.save(self.image.path)

# Create your models here.
