from django.contrib.auth.models import User, Group
from articleapp.models import Article
from rest_framework import serializers


# class UserSerializer(serializers.HyperlinkedModelSerializer):
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['url', 'username', 'email', 'groups']
        fields = '__all__'