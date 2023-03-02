from django.contrib.auth import authenticate
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=100,write_only=True)

    def create(self, validated_data):
        user = authenticate(username=validated_data['email'], password=validated_data['password'],
                            )
        if not user:
            raise serializers.ValidationError("Wrong Credentials")
        validated_data.update({'user': user})
        return user
