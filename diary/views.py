from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Diary
from django.urls import reverse_lazy


class DiaryListView(ListView):
    model = Diary
    paginated_by = 10
    ordering = ['-created_at']


class DiaryDetailView(DetailView):
    model = Diary


class DiaryCreateView(CreateView):
    model = Diary
    fields = ["author", "body"]


class DiaryUpdateView(UpdateView):
    model = Diary
    fields = ["author", "body"]


class DiaryDeleteView(DeleteView):
    model = Diary
    success_url = reverse_lazy("diary-list")