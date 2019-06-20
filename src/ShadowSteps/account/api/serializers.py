from rest_framework import serializers
from account.models import Profile, UserLanguage


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class LanguageSerializer(serializers.ModelSerializer):
    # language = serializers.SerializerMethodField()

    class Meta:
        model = UserLanguage
        fields = ('id', 'language', 'level')

    # def get_language(self, obj):
    #     return obj.get_language_display()
