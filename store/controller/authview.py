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

def urduloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/urdu')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/urdu')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/urdulogin')
        return render(request, 'urdu-store/auth/login.html')

def indonesianloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/indonesian')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/indonesian')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/indonesianlogin')
        return render(request, 'indonesian-store/auth/login.html')

def germanloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/german')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/german')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/germanlogin')
        return render(request, 'german-store/auth/login.html')

def japaneseloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/japanese')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/japanese')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/japaneselogin')
        return render(request, 'japanese-store/auth/login.html')

def nigerianloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/nigerian')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/nigerian')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/nigerianlogin')
        return render(request, 'nigerian-store/auth/login.html')

def marathiloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/marathi')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/marathi')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/marathilogin')
        return render(request, 'marathi-store/auth/login.html')

def teluguloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/telugu')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/telugu')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/telugulogin')
        return render(request, 'telugu-store/auth/login.html')

def turkishloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/turkish')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/turkish')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/turkishlogin')
        return render(request, 'turkish-store/auth/login.html')

def tamilloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/tamil')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/tamil')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/tamillogin')
        return render(request, 'tamil-store/auth/login.html')

def vietnameseloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/vietnamese')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/vietnamese')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/vietnameselogin')
        return render(request, 'vietnamese-store/auth/login.html')

def tagalogloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/tagalog')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/tagalog')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/tagaloglogin')
        return render(request, 'tagalog-store/auth/login.html')

def koreanloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/korean')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/korean')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/koreanlogin')
        return render(request, 'korean-store/auth/login.html')

def iranianloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/iranian')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/iranian')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/iranianlogin')
        return render(request, 'iranian-store/auth/login.html')

def hausaloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/hausa')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/hausa')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/hausalogin')
        return render(request, 'hausa-store/auth/login.html')

def swahililoginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/swahili')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/swahili')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/swahililogin')
        return render(request, 'swahili-store/auth/login.html')

def javaneseloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/javanese')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/javanese')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/javaneselogin')
        return render(request, 'javanese-store/auth/login.html')

def italianloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/italian')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/italian')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/italianlogin')
        return render(request, 'italian-store/auth/login.html')

def punjabiloginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,'You are already logged in')
        return redirect('/punjabi')
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/punjabi')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/punjabilogin')
        return render(request, 'punjabi-store/auth/login.html')