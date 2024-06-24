from rest_framework import serializers
from .models import MediaFile
from rest_framework import generics
from django.contrib.auth.models import User

class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ['id', 'user', 'file', 'uploaded_at']
        read_only_fields = ['user', 'uploaded_at']
        
    def get_download_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.file.url)
        return obj.file.url

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class MediaFileList(generics.ListAPIView):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileSerializer
