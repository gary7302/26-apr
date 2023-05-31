from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

def nigerianhome(request):
    category=NigerianCategory.objects.all()
    return render(request,'nigerian-store/index.html',{'category':category})


def nigeriandetails(request):
    return render(request,'nigerian-store/details.html')

def nigeriancomment(request,id):
    eachProduct=NigerianCategory.objects.get(id=id)
    form=NigerianCommentForm()
    context={'form':form,'eachProduct':eachProduct}
    return render(request,'nigerian-store/coment.html',context)

@login_required(login_url='nigerianlogin')
def nigerianaddcomment(request,id):
    if request.method == "POST":
        form=NigerianCommentForm(request.POST,request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = NigerianCategory.objects.get(id=id)
            d = NigerianComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,
                             comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('nigerian')
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
                return redirect('/nigerianlogin')
            except IntegrityError:
                messages.warning(request,'This username altreay in use. Please choose another')
    context={'form':form}
    return render(request,'nigerian-store/auth/register.html',context)

def nigeriangetpatch(request):
    return render(request,'nigerian-store/getpatch.html')

def nigerianusepatch(request):
    return render(request,'nigerian-store/usepatch.html')