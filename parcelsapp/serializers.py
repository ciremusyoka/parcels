from rest_framework import serializers
from .models import Parcels

class ParcelSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(source='sender.first_name', read_only=True)
    sender_email = serializers.EmailField(source='sender.email', read_only=True)
    transporter_name = serializers.CharField(source='transporter.first_name', read_only=True)
    class Meta:
        model = Parcels
        fields = ('id', 'sender_name', 'sender_email', 'sender', 'name', 'origin','transporter','transporter_name',
                  'destination', 'ParcelCost','receiver_name', 'receiver_phone', 'date', 'ParcelStatus')


class AddParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcels
        fields = ('id', 'sender', 'name', 'origin', 'destination')

class AcceptJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcels
        fields = ('id', 'TransporterResponse' ,'ParcelStatus')

    def validate(self, data):
        response = data["TransporterResponse"]
        status = data["ParcelStatus"]
        if not response or status != 'waiting':
            raise serializers.ValidationError('not Updated')
        return (data)

class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcels
        fields = ('id', 'SendingCost', 'CourierNumber' , 'ParcelStatus')

    def validate(self, data):
        cost = data["SendingCost"]
        number = data['CourierNumber']
        status = data["ParcelStatus"]
        if not cost or not number or status != 'ontransit':
            raise serializers.ValidationError('You must fill all the fields correctly')
        return (data)

class ReceivedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcels
        fields =('id', 'ParcelStatus', 'DeliveredTransporter')


class DeliveredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcels
        fields = ('id', 'DeliveredSender', 'ParcelStatus')

class SenderPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcels
        fields = ('sender', 'name', 'origin', 'destination', 'ParcelCost', 'ParcelStatus',
                  'SendingCost', 'CourierNumber', 'DeliveredSender','transporter')

class TransporterPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcels
        fields = ('ParcelStatus','DeliveredTransporter')


