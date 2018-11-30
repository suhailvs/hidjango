from django.urls import path, include

from rest_framework import routers

from . import views
from . import models

router = routers.DefaultRouter()
router.register(r'users', views.CURDViewSet.create_custom(model=models.User))
router.register(r'nuggets', views.NuggetList)
urlpatterns = [	
	path('', include(router.urls)),
]