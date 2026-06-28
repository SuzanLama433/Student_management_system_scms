from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    image = models.ImageField(upload_to='studentImage/')
    address = models.CharField(max_length=50)
    create_at = models.DateField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    
