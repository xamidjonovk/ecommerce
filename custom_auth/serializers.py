from rest_framework import serializers

class SMSSerializer(serializers.Serializer):
    phone_number = serializers.CharField()

class VerifySMSSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    verification_code = serializers.CharField()
