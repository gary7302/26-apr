from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

def tamilhome(request):
    category=TamilCategory.objects.all()
    return render(request,'tamil-store/index.html',{'category':category})


def tamildetails(request):
    return render(request,'tamil-store/details.html')

def tamilcomment(request,id):
    eachProduct=TamilCategory.objects.get(id=id)
    form=TamilCommentForm()
    context={'form':form,'eachProduct':eachProduct}
    return render(request,'tamil-store/coment.html',context)

@login_required(login_url='tamillogin')
def tamiladdcomment(request,id):
    if request.method == "POST":
        form=TamilCommentForm(request.POST,request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = TamilCategory.objects.get(id=id)
            d = TamilComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,
                             comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('tamil')
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
                return redirect('/tamillogin')
            except IntegrityError:
                messages.warning(request,'This username altreay in use. Please choose another')
    context={'form':form}
    return render(request,'tamil-store/auth/register.html',context)

def tamilgetpatch(request):
    return render(request,'tamil-store/getpatch.html')

def tamilusepatch(request):
    return render(request,'tamil-store/usepatch.html')