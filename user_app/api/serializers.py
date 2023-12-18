from rest_framework import serializers
from user_app.models import User


class UserSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    # photo = serializers.ImageField()
    # created_at = serializers.DateTimeField()
    # updated_at = serializers.DateTimeField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance

    # validation input data
    def validate_username(self, value):
        print(len(value))
        if len(value) < 2 :
            raise serializers.ValidationError('Name is to short')
        else:
            return value

