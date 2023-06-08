from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()



class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id_user= models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg=models.ImageField(upload_to='profile_file',default='blank.webp')
    location = models.CharField(max_length=100,blank=True)



# Create your models here.
