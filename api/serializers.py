# api/serializers.py

from rest_framework import serializers
from .models import docs



class DocSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    class Meta:
        """Map this serializer to a model and their fields."""
        model = docs
        fields = ('client_id', 'doc_name', 'date_created')
        read_only_fields = ('date_created', 'client_id')
