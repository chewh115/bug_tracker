from django.urls import path
from bug_tracker import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_view, name='login'),
    path('new-ticket/', views.new_ticket, name='new_ticket'),
    path('ticket-detail/<int:pk>/', views.ticket_detail, name='ticket_detail'),
    path('assign-to/<int:pk>/', views.assign_to, name='assign_to'),
    path('logout/', views.logout_view, name='logout'),
    # need path for ind. ticket
]