from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

def germanhome(request):
    category=GermanCategory.objects.all()
    return render(request,'german-store/index.html',{'category':category})


def germandetails(request):
    return render(request,'german-store/details.html')
@login_required(login_url='germanlogin')
def germancomment(request,id):
    eachProduct = GermanCategory.objects.get(id=id)

    form = GermanCommentForm()
    context = {'form': form, 'eachProduct': eachProduct}
    return render(request, 'german-store/coment.html', context)

def germanaddcomment(request,id):
    if request.method == "POST":
        form = GermanCommentForm(request.POST, request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = GermanCategory.objects.get(id=id)
            d = GermanComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('german')
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
                return redirect('/germanlogin')
            except IntegrityError:
                messages.warning(request,'This username has already taken. Choose different')
    context={'form':form}
    return render(request,'german-store/auth/register.html',context)

def germangetpatch(request):
    return render(request,'german-store/getpatch.html')

def germanusepatch(request):
    return render(request,'german-store/usepatch.html')