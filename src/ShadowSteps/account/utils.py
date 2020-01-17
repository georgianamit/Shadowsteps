from rest_framework import serializers
from collections import OrderedDict


class ChoicesField(serializers.ChoiceField):
    def __init__(self, *args, **kwargs):
        choices = kwargs.get('choices')
        self._choices = OrderedDict(choices)
        super(ChoicesField, self).__init__(*args, **kwargs)

    def to_representation(self, obj):
        return self._choices[obj]

    # def to_internal_value(self, data):
    #     return getattr(self._choices, data)
