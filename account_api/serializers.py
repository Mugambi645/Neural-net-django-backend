from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]
    
    def create(self, validated_data):

        """
        Create a new User instance.

        This is a override of the default `create` method provided by Django
        Rest Framework. We need to hash the password before saving the User
        instance.

        Args:
            validated_data (dict): Dict of validated data.

        Returns:
            User: The newly created User instance.
        """
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["passwor"]
        )
        return user