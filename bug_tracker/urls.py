from django.urls import path
from bug_tracker import views

urlpatterns = [
    path('', views.index, name='home')
]