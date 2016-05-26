from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def index(request):

    last_user = User.objects.order_by('-id').first().full_name
    return render(request, 'faceitweb/index.html', {'last_user': last_user })
