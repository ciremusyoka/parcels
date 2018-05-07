from django.conf.urls import url
from .views import CreateUserView, LoginUserView, UsersListView, RetrieveUpdateUsers, ChangePasswordView, ResetPasswordView

urlpatterns = [
    url(r'^register', CreateUserView.as_view(), name='register'),
    url(r'^login', LoginUserView.as_view(), name='login'),
    url(r'^users/$', UsersListView.as_view(), name='users'),
    url(r'^user/(?P<username>[a-z, A-Z, 0-9]+)$', RetrieveUpdateUsers.as_view(), name='edit-users'),
    url(r'^password$', ChangePasswordView.as_view(), name='password'),
    url(r'^reset_password$',ResetPasswordView.as_view(), name='reset_password'),
    # url(r'^token/', CustomObtainAuthToken.as_view()),
]