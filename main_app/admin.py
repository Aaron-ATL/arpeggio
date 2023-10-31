from .models import Lesson, Profile
from django.contrib import admin

# Register your models here.

admin.site.register([Profile, Lesson])