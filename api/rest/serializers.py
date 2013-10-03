from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest.models import Forum, Thread, Post


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ForumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Forum
        fields = ('title',)

class ThreadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Thread
        fields = ('title', 'forum', 'creator')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('thread', 'body')
