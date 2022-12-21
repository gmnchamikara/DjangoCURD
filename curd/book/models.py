from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField()
    author = models.CharField(max_length=30, default='Guest')
    email = models.EmailField(blank=True)
    description = models.TextField(default='Available in Library')
    
    def __str__(self):
        return self.name
    