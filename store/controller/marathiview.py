from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

def marathihome(request):
    category=MarathiCategory.objects.all()
    return render(request,'marathi-store/index.html',{'category':category})


def marathidetails(request):
    return render(request,'marathi-store/details.html')

def marathicomment(request,id):
    eachProduct=MarathiCategory.objects.get(id=id)
    form=MarathiCommentForm()
    context={'form':form,'eachProduct':eachProduct}
    return render(request,'marathi-store/coment.html',context)

@login_required(login_url='marathilogin')
def marathiaddcomment(request,id):
    if request.method == "POST":
        form=MarathiCommentForm(request.POST,request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = MarathiCategory.objects.get(id=id)
            d =MarathiComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,
                             comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('marathi')
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
                return redirect('/marathilogin')
            except IntegrityError:
                messages.warning(request,'This username altreay in use. Please choose another')
    context={'form':form}
    return render(request,'marathi-store/auth/register.html',context)

def marathigetpatch(request):
    return render(request,'marathi-store/getpatch.html')

def marathiusepatch(request):
    return render(request,'marathi-store/usepatch.html')