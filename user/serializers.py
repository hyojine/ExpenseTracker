from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from user.models import Users
# from user.validators import email_validator, password_check_validator, password_vaildator, profile_name_validator, phone_validator, address_validator


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_id'] = user.id
        token['username'] = user.username
        token['is_admin'] = user.is_admin

        return token

class SignUpSerializer(serializers.ModelSerializer):
    password_check = serializers.CharField(max_length=50, write_only=True)

    def validate(self, attrs):
        if attrs["password"]!=attrs["password_check"]:
            raise serializers.ValidationError({"message":"비밀번호를 확인해주세요"}) # ok

        attrs.pop("password_check", None)
        return super().validate(attrs)

    def create(self, validated_data):
        user = super().create(validated_data)
        password =user.password
        user.set_password(password)
        user.is_active =True
        if not user.username:
            user.username=user.email.split('@')[0]+str(user.id) # ok
        user.save()
        return user

    class Meta:
        model = Users
        fields = "__all__"