from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

def bengalihome(request):
    category=BengaliCategory.objects.all()
    return render(request,'bengali-store/index.html',{'category':category})

@login_required(login_url='bengalilogin')
def bengalicomment(request,id):
    eachProduct = BengaliCategory.objects.get(id=id)

    form = BengaliCommentForm()
    context = {'form': form, 'eachProduct': eachProduct}
    return render(request, 'bengali-store/coment.html', context)

def bengaliaddcomment(request,id):
    if request.method == "POST":
        form = BengaliCommentForm(request.POST, request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = BengaliCategory.objects.get(id=id)
            d = BengaliComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('bengali')
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
                return redirect('/bengalilogin')
            except IntegrityError:
                messages.warning(request,'This username already in use. Please choose another')
    context={'form':form}
    return render(request,'bengali-store/auth/register.html',context)

def bengalidetails(request):
    return render(request,'bengali-store/details.html')

def bengaligetpatch(request):
    return render(request,'bengali-store/getpatch.html')

def bengaliusepatch(request):
    return render(request,'bengali-store/usepatch.html')