from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('courses', courses, name='courses'),
    path('courses/<slug:course_slug>', course_detail, name='course-detail'),
]
