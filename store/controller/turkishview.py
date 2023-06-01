from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

def turkishhome(request):
    category=TurkishCategory.objects.all()
    return render(request,'turkish-store/index.html',{'category':category})


def turkishdetails(request):
    return render(request,'turkish-store/details.html')

def turkishcomment(request,id):
    eachProduct=TurkishCategory.objects.get(id=id)
    form=TurkishCommentForm()
    context={'form':form,'eachProduct':eachProduct}
    return render(request,'turkish-store/coment.html',context)

@login_required(login_url='turkishlogin')
def turkishaddcomment(request,id):
    if request.method == "POST":
        form=TurkishCommentForm(request.POST,request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = TurkishCategory.objects.get(id=id)
            d = TurkishComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,
                             comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('turkish')
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
                return redirect('/turkishlogin')
            except IntegrityError:
                messages.warning(request,'This username altreay in use. Please choose another')
    context={'form':form}
    return render(request,'turkish-store/auth/register.html',context)

def turkishgetpatch(request):
    return render(request,'turkish-store/getpatch.html')

def turkishusepatch(request):
    return render(request,'turkish-store/usepatch.html')