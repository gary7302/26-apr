from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
def portuguesehome(request):
    category=PortugueseCategory.objects.all()
    return render(request,'portuguese-store/index.html',{'category':category})


def portuguesecomment(request,id):
    eachProduct = PortugueseCategory.objects.get(id=id)

    form = PortugueseCommentForm()
    context = {'form': form, 'eachProduct': eachProduct}
    return render(request, 'portuguese-store/coment.html', context)

@login_required(login_url='portugueselogin')
def portugueseaddcomment(request,id):
    if request.method == "POST":
        form = PortugueseCommentForm(request.POST, request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = PortugueseCategory.objects.get(id=id)
            d = PortugueseComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('portuguese')
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
                return redirect('/portugueselogin')
            except IntegrityError:
                messages.warning(request,'This username already in use. Please choose another')
    context={'form':form}
    return render(request,'portuguese-store/auth/register.html',context)

def portuguesedetails(request):
    return render(request,'portuguese-store/details.html')

def portuguesegetpatch(request):
    return render(request,'portuguese-store/getpatch.html')

def portugueseusepatch(request):
    return render(request,'portuguese-store/usepatch.html')