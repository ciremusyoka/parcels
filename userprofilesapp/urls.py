from django.conf.urls import url
from .views import ProfileView, UpdateProfileView

urlpatterns = [
    url(r'^profile$', ProfileView.as_view(), name='profile'),
    url(r'^profile/(?P<pk>[0-9]+)$', UpdateProfileView, name='profileid'),
]