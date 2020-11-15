from django.urls import path, include
from .views import DiaryListAPIView, DiaryDetailAPIView

urlpatterns = [
    path('diaries/', DiaryListAPIView.as_view(), name="api-diary-list"),
    path('diaries/<int:pk>/', DiaryDetailAPIView.as_view(), name="api-diary-detail"),
]