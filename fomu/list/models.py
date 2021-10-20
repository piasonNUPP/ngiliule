from django.db import models

# Create your models here.
class Dimo(models.Model):

    fname =models.CharField(max_length=100,blank=True)
    
    course =models.CharField(max_length=100,blank=True)
    
    year =models.IntegerField(blank=True)
    
    place =models.CharField(max_length=100,blank=True)

    def _str_ (self):
        return self.fname

class Task(models.Model):

    title =models.CharField(max_length=100)
    
    dawa =models.CharField(max_length=100,blank=True)
    due =models.DateTimeField(auto_now_add=False, auto_now=False,blank=True, null=True)
    
    complete =models.BooleanField(default=False)
    
    created =models.DateTimeField(auto_now_add=True)

    def _str_ (self):
        return self.title
