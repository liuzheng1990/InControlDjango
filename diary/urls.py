from django.urls import path
from . import views



urlpatterns = [
    path('', views.DiaryListView.as_view(), name="diary-list"),
    path('<int:pk>/', views.DiaryDetailView.as_view(), name="diary-detail"),
    path('add/', views.DiaryCreateView.as_view(), name="diary-create"),
    path('<int:pk>/update/', views.DiaryUpdateView.as_view(), name="diary-update"),
    path('<int:pk>/delete/', views.DiaryDeleteView.as_view(), name="diary-delete"),
]