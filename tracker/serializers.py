from rest_framework import serializers
from .models import Tracker


class TrackerSerializer(serializers.ModelSerializer): #기본 조회
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.username
    
    class Meta:
        model = Tracker
        fields = ('expense','date','user')

class TrackerDetailSerializer(serializers.ModelSerializer): #상세조회
    class Meta:
          model = Tracker
          fields = '__all__'

class TrackerCreateSerializer(serializers.ModelSerializer): #생성
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.username
    
    class Meta:
        model = Tracker
        fields = ('expense','date','user','memo','category')

class TrackerUpdateSerializer(serializers.ModelSerializer): #수정
    class Meta:
        model = Tracker
        fields = ('expense','date','memo','category')

