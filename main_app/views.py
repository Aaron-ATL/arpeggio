from json import loads as json_loads
from .models import Lesson, User
from .forms import CustomAuthenticationForm
from .utils import webhook_is_verified, has_purchased_course, send_activation_email, create_user
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
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

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm

@csrf_exempt
def webhook(request):
    if webhook_is_verified(request.body, request.META.get('HTTP_X_SHOPIFY_HMAC_SHA256')):
        if has_purchased_course(str(request.body)):
            customer_email = json_loads(request.body)["email"].lower()
            if User.objects.filter(username=customer_email).exists():
                user = User.objects.get(username=customer_email)
                send_activation_email(user)
            else:
                create_user(customer_email)
    return HttpResponse(status=200)