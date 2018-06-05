from rest_framework import serializers
from .models import JobsModel

class JobsSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(source='sender.first_name', read_only=True)
    sender_phone = serializers.EmailField(source='sender.username', read_only=True)
    parcel_name = serializers.CharField(source='parcel.name', read_only=True)
    parcel_origin = serializers.CharField(source='parcel.origin', read_only=True)
    class Meta:
        model = JobsModel
        fields = ('id','sender_name', 'sender_phone', 'parcel_name', 'parcel_origin', 'sender', 'transporter',
                  'parcel','accepted', 'completed', 'date')