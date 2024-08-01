from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

# creating serializers

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['first_name', 'last_name','username','email','password','role']
    
    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user



class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    role = serializers.CharField(read_only=True)

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
            validation = {
                'email': user.email,
                'password': user.password,
                'role': user.role,
            }

            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")