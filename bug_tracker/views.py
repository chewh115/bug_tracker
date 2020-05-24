from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth import login, logout, authenticate
from datetime import datetime
from .forms import TicketForm, LoginForm, StatusForm
from .models import WorkTicket

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        tickets = WorkTicket.objects.all()
        return render(request, 'index.html', {'tickets': tickets})
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
                time_filed = datetime.utcnow(),
                description = new_ticket_info['description'],
                creator = request.user,
                status = 'New',
            )
            return HttpResponseRedirect(reverse('home'))
    form = TicketForm()
    return render(request, 'new_ticket.html', {'form': form})


def ticket_detail(request, pk):
    ticket = WorkTicket.objects.get(pk=pk)
    if request.method == "POST":
        form = StatusForm(request.POST)
        if form.is_valid():
            new_status = form.cleaned_data.get('status_change')
            ticket.status = new_status
            ticket.save()
            return HttpResponseRedirect(reverse('home'))
    form = StatusForm()
    return render(request, 'ticket_detail.html', {'form': form, 'ticket': ticket})


def assign_to(request, pk):
    ticket = WorkTicket.objects.get(pk=pk)
    ticket.assign_to = request.user
    ticket.status = 'In Progress'
    ticket.save()
    return HttpResponseRedirect(reverse('home'))


def logout_view(reqest):
    logout(reqest)
    return HttpResponseRedirect(reverse('home'))