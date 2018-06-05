from django.conf.urls import url
from .views import JobsView, MyJobsView

urlpatterns = [
    url(r'^jobs$', JobsView.as_view(), name='jobs'),
    url(r'^myjobs$', MyJobsView.as_view(), name='my_jobs'),
]