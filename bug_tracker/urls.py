from django.urls import path
from bug_tracker import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='login')
    # need path for ind. ticket
]