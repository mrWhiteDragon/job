from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('vacancy/<int:vacancy_id>/', views.vacancy_detail, name='vacancy_detail'),
]