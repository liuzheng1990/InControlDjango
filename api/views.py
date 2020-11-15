from rest_framework import generics
from diary import models as diary_models
from diary import serializers as diary_serializers


class DiaryListAPIView(generics.ListCreateAPIView):
    queryset = diary_models.Diary.objects.all().order_by("-created_at")
    serializer_class = diary_serializers.DiarySerializer


class DiaryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = diary_models.Diary.objects.all()
    serializer_class = diary_serializers.DiarySerializer