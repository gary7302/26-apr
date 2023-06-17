from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

def kannadahome(request):
    category=KannadaCategory.objects.all()
    return render(request,'kannada-store/index.html',{'category':category})
def kannadadetails(request):
    return render(request,'kannada-store/details.html')
def kannadacomment(request,id):
    eachProduct = KannadaCategory.objects.get(id=id)

    form = KannadaCommentForm()
    context = {'form': form, 'eachProduct': eachProduct}
    return render(request, 'kannada-store/coment.html', context)

@login_required(login_url='kannadalogin')
def kannadaaddcomment(request,id):
    if request.method == "POST":
        form = KannadaCommentForm(request.POST, request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = KannadaCategory.objects.get(id=id)
            d = KannadaComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('kannada')
    return HttpResponse('<h1>We are unable to add your comment</h1>')

def register(request):
    form=CustomUserForm()
    if request.method=="POST":
        form=CustomUserForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            try:
                user=User.objects.create_user(username=username,password=form.cleaned_data['password1'])
                user.save()
                return redirect('/kannadalogin')
            except IntegrityError:
                messages.warning(request,'This username has already taken. Choose different')
    context={'form':form}
    return render(request,'kannada-store/auth/register.html',context)

def kannadagetpatch(request):
    return render(request,'kannada-store/getpatch.html')

def kannadausepatch(request):
    return render(request,'kannada-store/usepatch.html')