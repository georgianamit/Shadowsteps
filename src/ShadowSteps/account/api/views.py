from rest_framework import generics
from account.models import Profile, UserLanguage
from .serializers import AccountSerializer, LanguageSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class AccountAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = AccountSerializer


class AccountListAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = AccountSerializer


class LanguageListAPIView(generics.ListCreateAPIView):
    queryset = UserLanguage.objects.all()
    serializer_class = LanguageSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data

        user = request.user
        language = validated_data['language']
        level = validated_data['level']
        u = UserLanguage.objects.filter(user=user, language=language)
        # print(validated_data, user, language, u, level)
        if not u:
            user_lng = UserLanguage(
                user=user, language=language, level=level)
            user_lng.save()
            return Response(serializer.data)
        else:
            if u.values_list("level", flat=True)[0] == level:
                raise ValidationError(
                    "This Language is already in your skill.")


class LanguageEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserLanguage.objects.all()
    serializer_class = LanguageSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    # def destroy(self, request, pk, *args, **kwargs):
    #     user_lang = self.get_object(pk)
    #     user_lang.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
