from django.db import models

# Create your models here.
class Picture(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    year=models.IntegerField()
    actors=models.CharField(max_length=250)
    category=models.CharField(max_length=250)
    link=models.URLField()
    img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name