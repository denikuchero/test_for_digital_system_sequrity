from rest_framework import serializers
from .models import *


class ListGuardObjectSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = GuardObject
        fields = "__all__"


class ListEventObjectSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = GuardObjectEvent
        fields = "__all__"


class ReportEventSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = GuardObjectEvent
        fields = ('rel_object_uuid', 'datetime', 'description')


class ReportSendSuccessSendEmailSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = LogEmail
        fields = "__all__"



class ReportLogEmailSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = LogEmail
        fields = "__all__"
