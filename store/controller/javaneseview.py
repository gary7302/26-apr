from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

def javanesehome(request):
    category=JavaneseCategory.objects.all()
    return render(request,'javanese-store/index.html',{'category':category})


def javanesedetails(request):
    return render(request,'javanese-store/details.html')

def javanesecomment(request,id):
    eachProduct=JapaneseCategory.objects.get(id=id)
    form=JavaneseCommentForm()
    context={'form':form,'eachProduct':eachProduct}
    return render(request,'javanese-store/coment.html',context)

@login_required(login_url='javaneselogin')
def javaneseaddcomment(request,id):
    if request.method == "POST":
        form=JavaneseCommentForm(request.POST,request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = JavaneseCategory.objects.get(id=id)
            d = JavaneseComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,
                             comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('javanese')
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
                return redirect('/javaneselogin')
            except IntegrityError:
                messages.warning(request,'This username already in use. Please choose another')
    context={'form':form}
    return render(request,'javanese-store/auth/register.html',context)

def javanesegetpatch(request):
    return render(request,'javanese-store/getpatch.html')

def javaneseusepatch(request):
    return render(request,'javanese-store/usepatch.html')