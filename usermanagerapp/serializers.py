from  rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.models import User, Group

# create user
class CreateUserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    def create (self, validated_data):
        user = get_user_model().objects.create(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password','id', 'first_name', 'last_name')

# login user
class LoginUserSerializer(serializers.ModelSerializer):
    username= serializers.CharField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'password','id')

    def validate(self, data):
        password = data["password"]
        username=data.get("username", None)
        if not username:
            raise serializers.ValidationError("username is required to login")
        user = get_user_model().objects.filter(Q(username=username))
        if user.exists():
            user_obj=user.first()
        else:
            raise serializers.ValidationError("This user doesn't exist")
        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError("incorrect password")

        return (data)


# retrive users
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('__all__')

# change users password
class ChangePasswordSerializer(serializers.ModelSerializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

