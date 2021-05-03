from django.db import models
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField

# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='thumb')
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(300, 200)],
        format='png',
        options={'quality': 60},
        autoconvert=True
    )

    def __str__(self) -> str:
        return self.name
