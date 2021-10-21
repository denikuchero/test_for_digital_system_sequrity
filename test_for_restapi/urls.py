"""test_for_restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app_restapi.views import *

router = routers.DefaultRouter()
# router.register(r'roles', RoleViewSet, basename='roles')
router.register(r'objects', ListGuardObject, basename='objects')
router.register(r'event', ListEventObject, basename='event')
router.register(r'report-event', ReportEvent, basename='report-event')
router.register(r'success-send-email', ReportSendSuccessSendEmail, basename='success-send-email')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v0/', include(router.urls))
    # path('api/v0/', include('rest_framework.urls'))
]
