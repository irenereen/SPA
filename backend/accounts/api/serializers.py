from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password  = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ['id','username', 'email', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
				{"password": "Password fields didn't match. "}
			)
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
			username=validated_data['username'],
			email=validated_data['email'],
			#profile_photo=validated_data['profile_photo']
		)

        user.set_password(validated_data['password'])
        user.save()

        return user

        

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None or password is None:
            raise serializers.ValidationError(
                'Both username and password are required to login.'
            )

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                'Invalid username or password.'
            )

        return {
            'username': user.username,
            'email': user.email,
            'tokens': self._get_tokens_for_user(user)
        }

    def _get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
