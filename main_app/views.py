from .models import Lesson
from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.

class LessonListView(ListView):
    template_name = "main_app/lesson_list_view.html"
    model = Lesson
    context_object_name = "lessons"
    ordering = ['number']

class LessonDetailView(DetailView):
    model = Lesson
    template_name = "main_app/lesson_detail_view.html"
    context_object_name = "current_lesson"