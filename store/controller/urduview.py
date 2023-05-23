from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

def urduhome(request):
    category=UrduCategory.objects.all()
    return render(request,'urdu-store/index.html',{'category':category})

@login_required(login_url='urdulogin')
def urdudetails(request):
    return render(request,'urdu-store/details.html')

def urducomment(request,id):
    eachProduct=UrduCategory.objects.get(id=id)
    form=UrduCommentForm()
    context={'form':form,'eachProduct':eachProduct}
    return render(request,'urdu-store/coment.html',context)

def urduaddcomment(request,id):
    if request.method == "POST":
        form=UrduCommentForm(request.POST,request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = UrduCategory.objects.get(id=id)
            d = UrduComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,
                             comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('urdu')
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
                return redirect('/urdulogin')
            except IntegrityError:
                messages.warning(request,'This username altreay in use. Please choose another')
    context={'form':form}
    return render(request,'urdu-store/auth/register.html',context)

def urdugetpatch(request):
    return render(request,'urdu-store/getpatch.html')

def urduusepatch(request):
    return render(request,'urdu-store/usepatch.html')