from django.conf.urls import url
from .views import ParcelsList, RetriveUpdateParcel

urlpatterns = [
    url(r'^parcels$', ParcelsList.as_view(), name='parcel'),
    url(r'^parcels/(?P<pk>[0-9]+)$', RetriveUpdateParcel.as_view(), name='parcelid')
]