from django.db import models
from pyuploadcare.dj.models import ImageField
# Create your models here.

# Creating Contact Model
class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=196)
    message = models.TextField()

    def __str__(self):
        return self.email
    
class Projects(models.Model):
    title = models.CharField(max_length = 31, blank = True)
    image = ImageField(blank=True, manual_crop="")
    description = models.TextField(blank=True)
    technologies = models.CharField(max_length=200, blank=True)
    livesite = models.CharField(max_length=200)
    githublink = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
    def save_image(self):
        self.save()
        
    def update_image(self):
        self.update()
        
    def delete_image(self,cls):
        cls.objects.get(id = self.id).delete()