from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

def vietnamesehome(request):
    category=VietnameseCategory.objects.all()
    return render(request,'vietnamese-store/index.html',{'category':category})


def vietnamesedetails(request):
    return render(request,'vietnamese-store/details.html')

def vietnamesecomment(request,id):
    eachProduct=VietnameseCategory.objects.get(id=id)
    form=VietnameseCommentForm()
    context={'form':form,'eachProduct':eachProduct}
    return render(request,'vietnamese-store/coment.html',context)

@login_required(login_url='vietnameselogin')
def vietnameseaddcomment(request,id):
    if request.method == "POST":
        form=VietnameseCommentForm(request.POST,request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = VietnameseCategory.objects.get(id=id)
            d = VietnameseComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,
                             comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('vietnamese')
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
                return redirect('/vietnameselogin')
            except IntegrityError:
                messages.warning(request,'This username altreay in use. Please choose another')
    context={'form':form}
    return render(request,'vietnamese-store/auth/register.html',context)

def vietnamesegetpatch(request):
    return render(request,'vietnamese-store/getpatch.html')

def vietnameseusepatch(request):
    return render(request,'vietnamese-store/usepatch.html')