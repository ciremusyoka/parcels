from  rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth.models import User, Group
from .models import Profile, Verification


#verivication code
class VerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verification
        fields = ['id', 'code']

#  profile serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user',  'Phone_Number', 'county', 'Transporter_Request',
                  'constituency', 'town','Id_No', 'Transporter_Accepted', 'photo',]

# update profile serializer
class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'Phone_Number', 'county', 'Transporter_Request',
                  'constituency', 'town', 'Id_No', 'photo']

# create user serializer
class CreateUserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    password=serializers.CharField(write_only=True)
    email = serializers.CharField(required=True)
    # verification_code = VerificationSerializer(required=True)

    def create (self, validated_data):
        # create user
        user = get_user_model().objects.create(
            username = validated_data['username'],
            email =  validated_data ['email'],
            first_name = validated_data['first_name'],
            last_name=validated_data['last_name'],
            # password = validated_data['password']
        )
        password = user.set_password(validated_data['password']),
        user.save()
        # create profile
        profile_data = validated_data.pop('profile')
        profile = Profile.objects.create(
            user=user,
            Phone_Number = profile_data['Phone_Number'],
            county = profile_data['county'],
            constituency = profile_data['constituency'],
            town = profile_data['town'],
            Id_No = profile_data['Id_No'],
            photo = profile_data['photo']
            )
        #generate verification code
        # verification_code_data = validated_data.pop('verification_code')
        # verification_code = Verification.objects.create(
        #     code = verification_code_data['code']
        # )
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password','id', 'first_name', 'last_name', 'profile',)


# update user details serializer
class UpdateUserSerializer(serializers.ModelSerializer):
    profile = UpdateProfileSerializer()
    class Meta:
        model = get_user_model()
        fields = ( 'id', 'first_name', 'last_name', 'email', 'profile')


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
    profile = ProfileSerializer(required=True)
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

    class Meta:
        model = get_user_model()
        fields = ('old_password', 'new_password', "id")

# reset user password
class ResetPasswordSerializer(serializers.ModelSerializer):
    username= serializers.CharField()
    email = serializers.CharField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'id')

    def validate(self, data):
        email = data.get("email", None)
        username=data.get("username", None)
        if not username and email:
            raise serializers.ValidationError("Both username and email are required to reset password")
        user = get_user_model().objects.filter(Q(username=username))
        email = get_user_model().objects.filter(Q(email=email))

        if user.exists():
            user_obj = user.first()
            # all = get_user_model().objects.all()
            # print(all)
            # print(user_obj)
        else:
            raise serializers.ValidationError("This user doesn't exist")
        if email.exists():
            pass
            # print (email)
        else:
            raise serializers.ValidationError("email doesn't exist")

        # if user_obj:
        #     if not user_obj.check_email(email):
        #         raise serializers.ValidationError("incorrect email")

        return (data)