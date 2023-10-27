from django.db import models
from django.db import connection


# Create your models here.
class students(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    sid = models.CharField(max_length=20)
    email = models.EmailField(max_length=64)
    
    courses = models.ManyToManyField("Course", blank=True,related_name='students')
    def __str__(self):
        return f"{self.first_name} {self.last_name} : { self.sid}  {self.email}"

class course(models.Model):
    cname = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.cname}"



