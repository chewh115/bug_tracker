from django.urls import path
from bug_tracker import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_view, name='login'),
    path('new-ticket/', views.new_ticket, name='new_ticket')
    # need path for ind. ticket
]