from rest_framework import generics, permissions
from account.models import Profile, UserLanguage
from .serializers import AccountSerializer, LanguageSerializer


class AccountAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = AccountSerializer


class AccountListAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = AccountSerializer


class LanguageListAPIView(generics.ListCreateAPIView):
    queryset = UserLanguage.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (permissions.IsAdminUser)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LanguageEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserLanguage.objects.all()
    serializer_class = LanguageSerializer
