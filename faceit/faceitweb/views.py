from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm
from .models import User

def index(request):
    return render(request, 'faceitweb/index.html')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = User(full_name=form.cleaned_data['full_name'])
            user.save()

            return HttpResponseRedirect('/')

    return render(request, 'faceitweb/index.html')


# def users(request):
#     return render(request, 'faceitweb/users.html', {'users': User.objects.all() })
