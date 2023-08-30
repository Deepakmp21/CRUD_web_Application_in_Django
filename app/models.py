from django.db import models

# Create your models here.


# Model Created
class Teacher(models.Model):
    Firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.CharField(max_length=50)



class Student(models.Model):
    Firstname =  models.CharField(max_length=50)
    Lastname =  models.CharField(max_length=50)
    Email =  models.EmailField(max_length=50)
    Contact =  models.IntegerField()
# This function is  used ti converting object into String
    def __str__(self) -> str:
        return self.Firstname
    
    
class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email= models.EmailField(max_length=50)
    contact = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class ImageData(models.Model):
    Imagename= models.CharField(max_length=50)
    Image= models.ImageField(upload_to="img/")