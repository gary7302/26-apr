from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

def punjabihome(request):
    category=PunjabiCategory.objects.all()
    return render(request,'punjabi-store/index.html',{'category':category})


def punjabidetails(request):
    return render(request,'punjabi-store/details.html')


def punjabicomment(request,id):
    eachProduct=PunjabiCategory.objects.get(id=id)
    form=PunjabiCommentForm()
    context={'form':form,'eachProduct':eachProduct}
    return render(request,'punjabi-store/coment.html',context)

@login_required(login_url='punjabilogin')
def punjabiaddcomment(request,id):
    if request.method == "POST":
        form=PunjabiCommentForm(request.POST,request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = PunjabiCategory.objects.get(id=id)
            d = PunjabiComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,
                             comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('punjabi')
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
                return redirect('/punjabilogin')
            except IntegrityError:
                messages.warning(request,'This username already in use. Please choose another')
    context={'form':form}
    return render(request,'punjabi-store/auth/register.html',context)

def punjabigetpatch(request):
    return render(request,'punjabi-store/getpatch.html')

def punjabiusepatch(request):
    return render(request,'punjabi-store/usepatch.html')