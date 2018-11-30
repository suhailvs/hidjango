# from django.shortcuts import render
# from django.db import models
from rest_framework import serializers, viewsets, mixins

def serializer_factory(mdl, fields="__all__", **kwargss):
    # https://stackoverflow.com/a/33137535/2351696
    class MySerializer(serializers.ModelSerializer):
        # created_by = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
        class Meta:
            model = mdl
        if fields:
            setattr(Meta, "fields", fields) #fields = fields
    return MySerializer

# Create your views here.
class CURDViewSet(
	mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet):
    # https://stackoverflow.com/a/26916875/2351696
    @classmethod
    def create_custom(self, **kwargs):
        class CustomViewSet(self):
            model = kwargs["model"]
            queryset = kwargs["model"].objects.all()
            serializer_class = serializer_factory(kwargs["model"])
        return CustomViewSet

from .models import Nugget, NuggetSerializer
from rest_framework.permissions import IsAuthenticated
class NuggetList(CURDViewSet):
    queryset = Nugget.objects.all()
    serializer_class = NuggetSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        req = serializer.context['request']
        serializer.save(created_by=req.user)
