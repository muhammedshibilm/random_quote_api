from django.db import models

# Create your models here.
class RandomData(models.Model):
    author = models.CharField(max_length=100)
    text = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.author
