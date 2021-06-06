from typing import SupportsRound
from django.db.models import base
from django.conf.urls import include, url
from django.urls.conf import path
from rest_framework import urlpatterns
from . import views
from django.conf.urls import url

from rest_framework.routers import SimpleRouter, DefaultRouter

router = SimpleRouter()
router.register(r'attacks', views.AttackViewSet, basename='test')

urlpatterns = []

urlpatterns += router.urls
