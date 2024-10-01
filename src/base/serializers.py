from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%D-%M-%Y', read_only=True)
    updated_at = serializers.DateTimeField(format='%D-%M-%Y', read_only=True)
