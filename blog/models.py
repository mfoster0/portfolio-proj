from django.db import models

# Create your models here.
class Blog(models.Model):
    #the names used for the variables below appear to need to match the original (database properties)
    #if you alter these, the process will error
    title = models.CharField(max_length=100)
    pubdate = models.DateTimeField()
    body = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='blogimages/') #other params available like size

    #this is used so that admin will display the title rather than just the blog id
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pubdate_short(self):
        return self.pubdate.strftime('%b %e %Y')

