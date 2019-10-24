from rest_framework import serializers
from .models import InstallationRequest, STATUS_CHOICE


class InstallationRequestSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=2000)
    appointment_date = serializers.DateField()
    date_created = serializers.DateField()
    date_modified = serializers.DateTimeField()
    status = serializers.CharField(max_length=2,  default='W')

    class Meta:
        model = InstallationRequest
        fields = '__all__'

    def create(self, validated_data):

        return InstallationRequest.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.address = validated_data.get('address', instance.address)
        instance.appointment_date = validated_data.get('appointment_date', instance.appointment_date)
        instance.date_created = validated_data.get('date_created', instance.ddate_created)
        instance.date_modified = validated_data.get('date_modified', instance.date_modified)

        instance.save()

        return instance
