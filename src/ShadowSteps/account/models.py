from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to = "avatars/", default="avatars/default-avatar.png")
    dob = models.DateField(blank=True, null=True)
    specialization = models.CharField(max_length=50,blank= True)
    bio = models.TextField(max_length=500, blank=True)


    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def Post_Save_User(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)

    

    