from rest_framework import serializers
from store_management.models import Stores

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model= Stores
        fields=["name", "code", "active", "created_at", "updated_at","quantity", "type", "gst","price"]
       