from django.db import models

class Location(models.Model):
    place = models.CharField(max_length=30)
    date = models.DateField()
    # image = models.ForeignKey(Image)

    def __str__(self):
        return self.place

class Category(models.Model):
    name=models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Image(models.Model):
    photo = models.ImageField(upload_to = 'images/', blank=True, null=True)
    name = models.CharField(max_length=30)
    details = models.TextField()
    category = models.ForeignKey(Category, blank=True, null=True)
    location = models.ManyToManyField(Location)

    @classmethod
    def search_by_name(cls, search_term):
        memoirs = cls.objects.filter(name__icontains=search_term)
        return memoirs
        
        


    def __str__(self):
        return self.name


