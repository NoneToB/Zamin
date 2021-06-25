from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='dashboard-home'),
    path('profile/', my_profile, name='dashboard-profile'),
    path('courses/', my_courses, name='dashboard-courses'),
    path('saved/', saved_courses, name='dashboard-saved'),
    path('comments/', comments, name='dashboard-comments'),
    path('attempts/', my_test_attempts, name='dashboard-attempts'),
]