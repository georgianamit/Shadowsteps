from django.urls import path, include
from .views import (
    AccountAPIView,
    AccountListAPIView,
    LanguageListAPIView,
    LanguageEditAPIView,
    FrameworkListAPIView,
    FrameworkEditAPIView,
    PlatformListAPIView,
    PlatformEditAPIView
)
from rest_framework import routers

app_name = "account-api"

urlpatterns = [
    path("account/", AccountListAPIView.as_view(), name='list'),
    path("languages/", LanguageListAPIView.as_view(), name='languages'),
    path("language/<int:pk>/", LanguageEditAPIView.as_view(), name='language-edit'),
    path("frameworks/", FrameworkListAPIView.as_view(), name='frameworks'),
    path("framework/<int:pk>/", FrameworkEditAPIView.as_view(),
         name='framework-edit'),
    path("platforms/", PlatformListAPIView.as_view(), name='platforms'),
    path("platform/<int:pk>/", PlatformEditAPIView.as_view(), name='platform-edit'),
    # path("<int:pk>/detail/", AccountAPIView.as_view, 'detail'),
    # path("<int:pk>/delete/", AccountAPIView.as_view, 'delete'),
]
