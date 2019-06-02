from django.contrib import admin
from .models import Profile, UserLanguage, UserFramework, UserPlatform
# Register your models here.

admin.site.register(Profile)
admin.site.register(UserLanguage)
admin.site.register(UserFramework)
admin.site.register(UserPlatform)

