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

class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        depth=1
        fields = ('id','title', 'threads',)

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        depth=2
        fields = ('title', 'forum', 'body', 'creator', 'posts')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('thread', 'body', 'creator')
