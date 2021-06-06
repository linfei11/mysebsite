"""
from rest_framework import serializers
from .models import Attack
from django.contrib.auth.models import User

class AttackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        #fields = ['insert_time', 'update_time', 'user', 'risk_level', 'input_type', 'rule_id', 'rule_type', 'rule_name', 'content', 'pcap_path', 'comment']
        fields = '__all__'
"""
from .models import Attack
from rest_framework import routers, serializers, viewsets

# 序列化器是用来定义API的表示形式。
class AttackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attack
        fields = '__all__'
