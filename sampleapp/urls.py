from django.urls import path, include

from rest_framework import routers

from .views import CURDViewSet
from . import models

router = routers.DefaultRouter()
router.register(r'users', CURDViewSet.create_custom(model=models.User))

urlpatterns = [	
	path('', include(router.urls)),
]