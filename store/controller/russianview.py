from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
def russianhome(request):
    category=RussianCategory.objects.all()
    return render(request,'russian-store/index.html',{'category':category})


def russiancomment(request,id):
    eachProduct = RussianCategory.objects.get(id=id)

    form = RussianCommentForm()
    context = {'form': form, 'eachProduct': eachProduct}
    return render(request, 'russian-store/coment.html', context)

@login_required(login_url='russianlogin')
def russianaddcomment(request,id):
    if request.method == "POST":
        form = RussianCommentForm(request.POST, request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = RussianCategory.objects.get(id=id)
            d = RussianComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('russian')
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
                return redirect('/russianlogin')
            except IntegrityError:
                messages.warning(request,'This username already in use. Please choose another')
    context={'form':form}
    return render(request,'russian-store/auth/register.html',context)

def russiandetails(request):
    return render(request,'russian-store/details.html')

def russiangetpatch(request):
    return render(request,'russian-store/getpatch.html')

def russianusepatch(request):
    return render(request,'russian-store/usepatch.html')