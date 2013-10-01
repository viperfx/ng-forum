from django.conf.urls import patterns, url, include
from rest_framework import routers
from rest import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/get-token/', 'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^api/token-auth/', views.AuthView.as_view())
)
