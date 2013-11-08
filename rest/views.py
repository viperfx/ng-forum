from django.contrib.auth.models import User, Group
from rest.models import Forum, Thread, Post
from rest_framework import viewsets
from rest.serializers import UserSerializer, GroupSerializer, ForumSerializer, ThreadSerializer, PostSerializer
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from annoying.decorators import render_to
from rest_framework.decorators import api_view
@render_to('index.html')
def home(request):
    print request.user
    return {}


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ForumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer

class ThreadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

    def create(self, request):
        topic = Thread(body=request.DATA['body'], creator=User.objects.get(pk=request.DATA['creator']), forum=Forum.objects.get(pk=request.DATA['forum']), title=request.DATA['title'])
        topic.save()
        serializer = ThreadSerializer(topic)
        print serializer.data
        return Response({"url":"/forum/%d/thread/%d" % (serializer.data['forum']['id'], serializer.data['id'])})

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer



class AuthView(APIView):
    authentication_classes = (BasicAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)


@api_view(['POST'])
def ajax_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
      if user.is_active:
          login(request, user)
          return Response({"status" : "true"})
      else:
          return Response( {"status" : "false", "reason" : "You need to activate your account. Please check your email"})
    else:
          return Response({"status" : "false", "reason" : "Invalid username/password"})
