from django.conf.urls import url
from .views import (ParcelsList, RetrieveUpdateParcel, CourierView, AcceptJobView,
                    ReceivedView, DeliveredView, UserParcelsList)

urlpatterns = [
    url(r'^parcels$', ParcelsList.as_view(), name='parcel'),
    url(r'^parcels/(?P<pk>[0-9]+)$', RetrieveUpdateParcel.as_view(), name='ParcelId'),
    url(r'^userparcels$', UserParcelsList.as_view(), name='userparcels'),
    url(r'^acceptjob/(?P<pk>[0-9]+)$', AcceptJobView.as_view(), name='AcceptJob'),
    url(r'^courier/(?P<pk>[0-9]+)$', CourierView.as_view(), name='Courier'),
    url(r'^received/(?P<pk>[0-9]+)$', ReceivedView.as_view(), name='received'),
    url(r'^delivered/(?P<pk>[0-9]+)$', DeliveredView.as_view(), name='delivered'),
]