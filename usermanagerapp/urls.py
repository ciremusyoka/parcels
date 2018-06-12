from django.conf.urls import url
from .views import CreateUserView, LoginUserView, UsersListView, RetrieveUpdateUsers, ChangePasswordView,\
    ResetPasswordView, FilterTransporters, CreateProfileView, RetrieveUserIDView

urlpatterns = [
    url(r'^register', CreateUserView.as_view(), name='register'),
    url(r'^profile', CreateProfileView.as_view(), name='profile'),
    url(r'^login', LoginUserView.as_view(), name='login'),
    url(r'^users$', UsersListView.as_view(), name='users'),
    url(r'^transporters$', FilterTransporters.as_view(), name='transporter'),
    url(r'^user/(?P<username>[a-z, A-Z, 0-9]+)$', RetrieveUpdateUsers.as_view(), name='edit-users'),
    url(r'^user_id/(?P<username>[a-z, A-Z, 0-9]+)$', RetrieveUserIDView.as_view(), name='user_id'),
    url(r'^change_password$', ChangePasswordView.as_view(), name='password'),
    url(r'^reset_password$',ResetPasswordView.as_view(), name='reset_password'),
    # url(r'^token/', CustomObtainAuthToken.as_view()),
]