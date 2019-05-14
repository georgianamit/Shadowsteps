from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to = user_directory_path, default="avatars/default-avatar.png")
    dob = models.DateField(blank=True, null=True)
    phone_no = models.CharField(max_length=10, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,blank= True)
    website = models.CharField(max_length=30, blank= True)
    motto = models.CharField(max_length=150, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    specialization = models.CharField(max_length=50,blank= True)

    address = models.CharField(max_length=512, blank=True)
    city = models.CharField(max_length=128, blank=True)
    state = models.CharField(max_length=128, blank=True)
    zip_code = models.CharField(max_length=16, blank=True)

    high_school = models.CharField(max_length=512, blank=True)
    hs_year = models.CharField(max_length=4, blank=True)
    hs_percentage = models.CharField(max_length=5, blank=True)


    g_college = models.CharField(max_length=512, blank=True)
    g_degree = models.CharField(max_length=100, blank=True)
    g_branch = models.CharField(max_length=50, blank=True)    
    g_year = models.CharField(max_length=4, blank=True)
    g_cgpa = models.CharField(max_length=5, blank=True)

    pg_college = models.CharField(max_length=512, blank=True)
    pg_degree = models.CharField(max_length=100, blank=True)
    pg_branch = models.CharField(max_length=50, blank=True)    
    pg_year = models.CharField(max_length=4, blank=True)
    pg_cgpa = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def Post_Save_User(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)

    

    