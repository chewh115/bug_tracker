from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import TicketForm, LoginForm
from .models import WorkTicket

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    return redirect("/login/")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user_info = form.cleaned_data
            user = authenticate(
                request,
                username = user_info['username'],
                password = user_info['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def new_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            new_ticket_info = form.cleaned_data
            WorkTicket.objects.create(
                title = new_ticket_info['title'],
                time_filed = new_ticket_info['time_filed'],
                description = new_ticket_info['description'],
                creator = request.user,
                status = new_ticket_info['status'],
            )
            message = "New ticket added"
            return HttpResponseRedirect(reverse('home'))
    form = TicketForm()
    return render(request, 'new_ticket.html', {'form': form})