from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to = "avatars/", default="avatars/default-avatar.png")
    dob = models.DateField(blank=True, null=True)
    phone_no = models.CharField(max_length=10, blank=True)
    gender = models.CharField(max_length=30,blank= True)
    website = models.CharField(max_length=30, blank= True)
    motto = models.CharField(max_length=150, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    specialization = models.CharField(max_length=50,blank= True)
    
    address = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64, blank=True)
    state = models.CharField(max_length=64, blank=True)
    zip_code = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def Post_Save_User(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)

    

    