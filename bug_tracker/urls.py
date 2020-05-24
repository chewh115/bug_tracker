from django.urls import path
from bug_tracker import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login_view, name='login'),
    path('new-ticket/', views.new_ticket, name='new_ticket'),
    path('ticket-detail/<int:pk>/', views.ticket_detail, name='ticket_detail'),
    path('assign-to/<int:pk>/', views.assign_to, name='assign_to'),
    path('completed-by/<int:pk>/', views.completed_by, name='completed_by'),
    path('invalid/<int:pk>/', views.invalid, name='invalid'),
    path('user-detail/<int:id>/', views.user_detail, name='user_detail'),
    path('logout/', views.logout_view, name='logout'),
    # need path for ind. ticket
]