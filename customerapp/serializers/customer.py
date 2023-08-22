from rest_framework import serializers


class CustomerSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class CreateCustomerSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()    


class CustomerProductListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) 
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)   
    price = serializers.CharField(read_only=True)  


class CreateProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()   
    price = serializers.CharField()         


class DisableSerializer(serializers.Serializer):
    id = serializers.IntegerField()          