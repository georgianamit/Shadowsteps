from django.urls import path, include
from account.views import ProfileView, settingView, signInView, signUpView

app_name = "account"

urlpatterns = [
    path("profile/<str:slug>/", ProfileView.as_view(), name="profile"),
    path("setting/", settingView, name="setting"),
    path("signin/", signInView, name="signin"),
    path("signup/", signUpView, name="signup"),
]
