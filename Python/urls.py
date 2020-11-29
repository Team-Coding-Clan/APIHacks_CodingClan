from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('questions/', views.questions, name='questions'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('save/', views.save, name='save'),

]
