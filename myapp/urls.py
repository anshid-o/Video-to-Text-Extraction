from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('extract_text', views.extract_text, name='extract_text'),
    path('download/', views.download_output_file, name='download_output_file'),
]
