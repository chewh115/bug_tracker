from django.shortcuts import render, reverse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'index.html')