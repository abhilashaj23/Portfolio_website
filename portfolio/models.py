from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phoneNumber=models.CharField(max_length=10)
    description=models.TextField()

    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=180)
    description=models.TextField()
    authname=models.CharField(max_length=15)
    img=models.ImageField(upload_to='Blog', blank=True, null=True)
    time_stamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
