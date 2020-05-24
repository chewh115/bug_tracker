from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth import login, logout, authenticate
from datetime import datetime
from .forms import TicketForm, LoginForm, StatusForm
from .models import MyUser, WorkTicket

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
                time_filed = datetime.now(),
                description = new_ticket_info['description'],
                creator = request.user,
                status = 'New',
            )
            return HttpResponseRedirect(reverse('home'))
    form = TicketForm()
    return render(request, 'new_ticket.html', {'form': form})


def ticket_detail(request, id):
    ticket = WorkTicket.objects.get(id=id)
    return render(request, 'ticket_detail.html', {'ticket': ticket})


def assign_to(request, id):
    ticket = WorkTicket.objects.get(id=id)
    ticket.assigned_to = request.user
    ticket.status = 'In Progress'
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail', args=(id,)))


def completed_by(request, id):
    ticket = WorkTicket.objects.get(id=id)
    ticket.completed_by = request.user
    ticket.status = 'Done'
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail', args=(id,)))


def invalid(request, id):
    ticket = WorkTicket.objects.get(id=id)
    ticket.status = 'Invalid'
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail', args=(id,)))


def user_detail(request, id):
    info = {}
    user = MyUser.objects.get(id=id)
    submitted = WorkTicket.objects.filter(creator_id = id)
    assigned = WorkTicket.objects.filter(assigned_to_id = id)
    completed = WorkTicket.objects.filter(completed_by_id = id)
    info['user'] = user
    info['submitted'] = submitted
    info['assigned'] = assigned
    info['completed'] = completed
    return render(request, 'user_detail.html', info)


def ticket_edit(request, id):
    ticket = WorkTicket.objects.get(id=id)
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            updated_ticket = form.cleaned_data
            ticket.title = updated_ticket['title']
            ticket.description = updated_ticket['description']
            ticket.save()
            return HttpResponseRedirect(reverse('ticket_detail', args=(id,)))
    form = TicketForm(initial = {
        'title': ticket.title,
        'description': ticket.description
    })
    return render(request, 'ticket_edit.html', {'form': form, 'ticket': ticket})

def logout_view(reqest):
    logout(reqest)
    return HttpResponseRedirect(reverse('home'))