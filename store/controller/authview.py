from django.shortcuts import render,redirect
from django.contrib import messages
from store.forms import *
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError

def register(request):
    form=CustomUserForm()
    if request.method == 'POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                user = User.objects.create_user(username=username, password=form.cleaned_data['password1'])
                user.save()
                return redirect('/login')
            except IntegrityError:
                form.add_error('username', 'This username already exists. Please choose a different one.')
    context={'form':form}
    return render(request,'store/auth/register.html',context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/login')
        return render(request, 'store/auth/login.html')

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Logged out successfully')
    return redirect('/')

def frenchloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/french')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/french')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/frenchlogin')
        return render(request, 'french-store/auth/login.html')

def hindiloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/hindi')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/hindi')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/hindilogin')
        return render(request, 'hindi-store/auth/login.html')

def chineseloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/chinese')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/chinese')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/chineselogin')
        return render(request, 'chinese-store/auth/login.html')

def spanishloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/spanish')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/spanish')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/spanishlogin')
        return render(request, 'spanish-store/auth/login.html')

def arabicloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/arabic')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/arabic')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/arabiclogin')
        return render(request, 'arabic-store/auth/login.html')

def bengaliloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/bengali')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/bengali')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/bengalilogin')
        return render(request, 'bengali-store/auth/login.html')

def russianloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/russian')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/russian')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/russianlogin')
        return render(request, 'russian-store/auth/login.html')

def portugueseloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/portuguese')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/portuguese')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/portugueselogin')
        return render(request, 'portuguese-store/auth/login.html')