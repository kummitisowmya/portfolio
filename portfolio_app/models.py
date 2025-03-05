from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=100)
    bio=models.TextField(max_length=1000)
    contact=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    linkedin=models.URLField()
    profile=models.ImageField(upload_to="media/",blank=True)
    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True)


    def __str__(self):
        return self.title
