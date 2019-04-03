from django.urls import path, include
from account.views import profileView, settingView, signInView, signUpView, signOutView

app_name = "account"

urlpatterns = [
    path("profile/<str:slug>/", profileView, name="profile"),
    path("setting/", settingView, name="setting"),
    path("signin/", signInView, name="signin"),
    path("signup/", signUpView, name="signup"),
    path("signout/", signOutView, name="signout")
]
