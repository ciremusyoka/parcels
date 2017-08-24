from django.conf.urls import url
from .views import CreateUserView, LoginUserView, UsersListView, RetrieveUpdateUsers, ChangePasswordView

urlpatterns = [
    url(r'^register', CreateUserView.as_view(), name='register'),
    url(r'^login', LoginUserView.as_view(), name='login'),
    url(r'^users/$', UsersListView.as_view(), name='users'),
    url(r'^users/(?P<pk>[0-9]+)$', RetrieveUpdateUsers.as_view(), name='edit-users'),
    url(r'^password$',ChangePasswordView.as_view(), name='password'),
]