from rest_framework import serializers
from account.models import Profile, UserLanguage
from account.choices import LANGUAGE_CHOICES
from account.utils import ChoicesField
from rest_framework.validators import UniqueTogetherValidator


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class LanguageSerializer(serializers.ModelSerializer):
    # language = serializers.SerializerMethodField()
    language = ChoicesField(
        choices=LANGUAGE_CHOICES)

    class Meta:
        model = UserLanguage
        fields = ('id', 'language', 'level')
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=UserLanguage.objects.all(),
        #         fields=('language', 'level')
        #     )
        # ]

    # def get_language(self, obj):
    #     return obj.get_language_display()

    # def to_internal_value(self, data):
    #     return data
