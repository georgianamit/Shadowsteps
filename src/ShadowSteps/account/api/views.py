from rest_framework import generics, status
from account.models import Profile, UserLanguage, UserPlatform, UserFramework
from .serializers import AccountSerializer, LanguageSerializer, FrameworkSerializer, PlatformSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.exceptions import ValidationError


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

    # def perform_create(self, serializer):
    #     return serializer.save(user=self.request.user)

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
            # user_lng = UserLanguage(
            #     user=user, language=language, level=level)
            # obj = user_lng.save()

            obj = serializer.save(user=self.request.user)
            serializer.validated_data['id'] = obj.id
            return Response(serializer.data)
        else:
            if u.values_list("level", flat=True)[0] == level:
                return Response({'msg': "You already have this language in your skills."}, status=status.HTTP_403_FORBIDDEN)
            else:
                u.update(level=level)
                return Response({'msg': "Your skill have been updated."},
                                status=status.HTTP_205_RESET_CONTENT)


class LanguageEditAPIView(generics.RetrieveDestroyAPIView):
    queryset = UserLanguage.objects.all()
    serializer_class = LanguageSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    # def destroy(self, request, pk, *args, **kwargs):
    #     user_lang = self.get_object(pk)
    #     user_lang.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class FrameworkListAPIView(generics.ListCreateAPIView):
    queryset = UserFramework.objects.all()
    serializer_class = FrameworkSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data

        user = request.user
        framework = validated_data['framework']
        level = validated_data['level']
        u = UserFramework.objects.filter(user=user, framework=framework)
        if not u:
            obj = serializer.save(user=self.request.user)
            serializer.validated_data['id'] = obj.id
            return Response(serializer.data)
        else:
            if u.values_list("level", flat=True)[0] == level:
                return Response({'msg': "You already have this language in your skills."}, status=status.HTTP_403_FORBIDDEN)
            else:
                u.update(level=level)
                return Response({'msg': "Your skill have been updated."},
                                status=status.HTTP_205_RESET_CONTENT)


class FrameworkEditAPIView(generics.RetrieveDestroyAPIView):
    queryset = UserFramework.objects.all()
    serializer_class = FrameworkSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


class PlatformListAPIView(generics.ListCreateAPIView):
    queryset = UserPlatform.objects.all()
    serializer_class = PlatformSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data

        user = request.user
        platform = validated_data['platform']
        level = validated_data['level']
        u = UserPlatform.objects.filter(user=user, platform=platform)
        if not u:
            obj = serializer.save(user=self.request.user)
            serializer.validated_data['id'] = obj.id
            return Response(serializer.data)
        else:
            if u.values_list("level", flat=True)[0] == level:
                return Response({'msg': "You already have this language in your skills."}, status=status.HTTP_403_FORBIDDEN)
            else:
                u.update(level=level)
                return Response({'msg': "Your skill have been updated."},
                                status=status.HTTP_205_RESET_CONTENT)


class PlatformEditAPIView(generics.RetrieveDestroyAPIView):
    queryset = UserPlatform.objects.all()
    serializer_class = PlatformSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
