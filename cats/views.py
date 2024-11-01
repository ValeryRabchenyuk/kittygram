# Обновлённый views.py на вьюсете ModelViewSet

from rest_framework import viewsets 

from .models import Cat
from .serializers import CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

"""
в поле queryset задаётся выборка объектов модели, с которой будет работать вьюсет;

в поле serializer_class указывается, какой сериализатор будет применён для валидации и сериализации.

"""