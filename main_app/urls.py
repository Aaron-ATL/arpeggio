from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import (
    LessonListView,
    LessonDetailView,
    # signup,
    # webhook,
)

urlpatterns = [
    path('', login_required(LessonListView.as_view()), name='index'),
    path('lesson/<int:pk>/', login_required(LessonDetailView.as_view()), name='lesson'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('signup/', signup, name='signup'),
    # path('webhook/', webhook),
]