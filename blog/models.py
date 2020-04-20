from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    pubdate = models.DateTimeField()
    body = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='blogimages/') #other params available like size
