from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

def teluguhome(request):
    category=TeluguCategory.objects.all()
    return render(request,'telugu-store/index.html',{'category':category})


def telugudetails(request):
    return render(request,'telugu-store/details.html')

def telugucomment(request,id):
    eachProduct=TeluguCategory.objects.get(id=id)
    form=TeluguCommentForm()
    context={'form':form,'eachProduct':eachProduct}
    return render(request,'telugu-store/coment.html',context)

@login_required(login_url='telugulogin')
def teluguaddcomment(request,id):
    if request.method == "POST":
        form=TeluguCommentForm(request.POST,request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = TeluguCategory.objects.get(id=id)
            d = TeluguComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,
                             comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('telugu')
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
                return redirect('/telugulogin')
            except IntegrityError:
                messages.warning(request,'This username altreay in use. Please choose another')
    context={'form':form}
    return render(request,'telugu-store/auth/register.html',context)

def telugugetpatch(request):
    return render(request,'telugu-store/getpatch.html')

def teluguusepatch(request):
    return render(request,'telugu-store/usepatch.html')