from ast import Not
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def login(request):
    form = AuthenticationForm()
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            request.session['pk'] = user.pk
            
            return redirect()
        return render(request, "auth.html", {'form': form})

