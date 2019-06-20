from django.urls import path, include
from .views import (
    AccountAPIView,
    AccountListAPIView,
    LanguageListAPIView,
    LanguageEditAPIView,
)
from rest_framework import routers

app_name = "account-api"

urlpatterns = [
    path("account/", AccountListAPIView.as_view(), name='list'),
    path("languages/", LanguageListAPIView.as_view(), name='languages'),
    path("languages/<int:pk>/", LanguageEditAPIView.as_view(), name='languages-edit'),
    # path("<int:pk>/detail/", AccountAPIView.as_view, 'detail'),
    # path("<int:pk>/delete/", AccountAPIView.as_view, 'delete'),
]
