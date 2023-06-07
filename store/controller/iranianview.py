from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

def iranianhome(request):
    category=IranianCategory.objects.all()
    return render(request,'iranian-store/index.html',{'category':category})


def iraniandetails(request):
    return render(request,'iranian-store/details.html')

def iraniancomment(request,id):
    eachProduct=IranianCategory.objects.get(id=id)
    form=IranianCommentForm()
    context={'form':form,'eachProduct':eachProduct}
    return render(request,'iranian-store/coment.html',context)

@login_required(login_url='iranianlogin')
def iranianaddcomment(request,id):
    if request.method == "POST":
        form=IranianCommentForm(request.POST,request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = IranianCategory.objects.get(id=id)
            d = IranianComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,
                             comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('iranian')
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
                return redirect('/iranianlogin')
            except IntegrityError:
                messages.warning(request,'This username already in use. Please choose another')
    context={'form':form}
    return render(request,'iranian-store/auth/register.html',context)

def iraniangetpatch(request):
    return render(request,'iranian-store/getpatch.html')

def iranianusepatch(request):
    return render(request,'iranian-store/usepatch.html')