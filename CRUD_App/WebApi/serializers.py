from rest_framework import serializers
from django.contrib.auth.models import User

class UserCreate(serializers.ModelSerializer):
  # We are writing this becoz we need confirm password field in our Registratin Request
  password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
  class Meta:
    model = User
    fields=['email', 'username', 'password', 'password2']
    extra_kwargs={
      'password':{'write_only':True}
    }

  # Validating Password and Confirm Password while Registration
  def validate(self, attrs):
    password = attrs.get('password')
    password2 = attrs.get('password2')
    if password != password2:
      raise serializers.ValidationError("Password and Confirm Password doesn't match")
    if not attrs.get('email'):
      raise serializers.ValidationError("Email is Not given.")  
    return attrs

  def create(self, validated_data):
    
    username = validated_data['username']
    email = validated_data['email']
    password = validated_data['password']
    user_obj = User(
        username=username,
        email=email
    )
    user_obj.set_password(password)
    user_obj.save()
    return validated_data