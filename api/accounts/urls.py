from django.conf.urls import url
from api.accounts import views

urlpatterns = [
    url(r'login/$', views.LoginView.as_view(), name='login'),
]
