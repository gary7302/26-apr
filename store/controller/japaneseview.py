from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

def japanesehome(request):
    category=JapaneseCategory.objects.all()
    return render(request,'japanese-store/index.html',{'category':category})


def japanesedetails(request):
    return render(request,'japanese-store/details.html')
@login_required(login_url='japaneselogin')
def japanesecomment(request,id):
    eachProduct=JapaneseCategory.objects.get(id=id)
    form=JapaneseCommentForm()
    context={'form':form,'eachProduct':eachProduct}
    return render(request,'japanese-store/coment.html',context)

def japaneseaddcomment(request,id):
    if request.method == "POST":
        form=JapaneseCommentForm(request.POST,request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = JapaneseCategory.objects.get(id=id)
            d = JapaneseComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,
                             comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('japanese')
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
                return redirect('/japaneselogin')
            except IntegrityError:
                messages.warning(request,'This username altreay in use. Please choose another')
    context={'form':form}
    return render(request,'japanese-store/auth/register.html',context)

def japanesegetpatch(request):
    return render(request,'japanese-store/getpatch.html')

def japaneseusepatch(request):
    return render(request,'japanese-store/usepatch.html')