from ast import Not
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import CodeForm
from .models import CustomUser

@login_required
def home_view(request):
    return render(request, "userauth/home.html")



def login_view(request):
    form = AuthenticationForm()
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            request.session['pk'] = user.pk
            
            return redirect('verify')
        return render(request, "userauth/uth.html", {'form': form})

def verify_view(request):
    form = CodeForm()
    pk = request.session.get('pk')
    if pk:
        user = CustomUser.objects.get(pk=pk)
        code = user.code
        user_code = f"{user.username}: {user.code}"

        if not request.POST:
            # SEND SMS
            print(user_code)
        if form.is_valid():
            num = form.cleaned_data.get('number')
            if str(code) == num:
                code.save()
                login(request, user)
                return redirect('home')
            else:
                return redirect('login')

    return render(request, "userauth/verify.html", {'form': form})
    # if request.method=="POST":
        # form = CodeForm(request.POST)
        # if form.is_valid():
        #     code = form.cleaned_data.get('number')
        #     if code == user.code:
        #         user.is_active = True
        #         user.save()
        #         return redirect('/')
        #     else:
        #         return render(request, "auth.html", {'form': form})