from django.conf.urls import patterns, url, include
from rest_framework import routers
from rest import views
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'forums', views.ForumViewSet)
router.register(r'threads', views.ThreadViewSet)
router.register(r'posts', views.PostViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',

    url(r'^api/', include(router.urls)),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/get-token/', 'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^api/basicauth/', views.AuthView.as_view()),
    url(r'^api/login/', views.ajax_login),
    url(r'^$', views.home),
)
