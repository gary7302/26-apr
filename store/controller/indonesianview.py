from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

def indonesianhome(request):
    category=IndonesianCategory.objects.all()
    return render(request,'indonesian-store/index.html',{'category':category})


def indonesiandetails(request):
    return render(request,'indonesian-store/details.html')

@login_required(login_url='indonesianlogin')
def indonesiancomment(request,id):
    eachProduct = IndonesianCategory.objects.get(id=id)

    form = IndonesianCommentForm()
    context = {'form': form, 'eachProduct': eachProduct}
    return render(request, 'indonesian-store/coment.html', context)

def indonesianaddcomment(request,id):
    if request.method == "POST":
        form = IndonesianCommentForm(request.POST, request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = IndonesianCategory.objects.get(id=id)
            d = IndonesianComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('indonesian')
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
                return redirect('/indonesianlogin')
            except IntegrityError:
                messages.warning(request,'This username has already taken. Choose different')
    context={'form':form}
    return render(request,'indonesian-store/auth/register.html',context)

def indonesiangetpatch(request):
    return render(request,'indonesian-store/getpatch.html')

def indonesianusepatch(request):
    return render(request,'indonesian-store/usepatch.html')