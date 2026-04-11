from django.urls import path
from .views import student_dashboard
from . import views

urlpatterns = [
    path('dashboard/', student_dashboard, name='student_dashboard'),
    path('officer/', views.officer_dashboard, name='officer_dashboard'),
]