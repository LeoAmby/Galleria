from django.db import models

class Image(models.Model):
    photo = models.ImageField(upload_to = 'images/', blank=True, null=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    # location = models.ForeignKey(location)
    # category = models.ForeignKey(category)
