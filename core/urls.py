from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from api.accounts import views as account_views

# Setup the ViewSet Router
router = DefaultRouter()
router.register(r'users', account_views.UserViewSet)

urlpatterns = [
    # Core Routed URLs
    url(r'^api/v1/', include(router.urls)),

    # Auth URLs
    url(r'^api/v1/auth/', include('api.accounts.urls')),

    # Browsable API
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
