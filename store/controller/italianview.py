from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

def italianhome(request):
    category=ItalianCategory.objects.all()
    return render(request,'italian-store/index.html',{'category':category})


def italiandetails(request):
    return render(request,'italian-store/details.html')

def italiancomment(request,id):
    eachProduct=ItalianCategory.objects.get(id=id)
    form=ItalianCommentForm()
    context={'form':form,'eachProduct':eachProduct}
    return render(request,'italian-store/coment.html',context)

@login_required(login_url='italianlogin')
def italianaddcomment(request,id):
    if request.method == "POST":
        form=ItalianCommentForm(request.POST,request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = ItalianCategory.objects.get(id=id)
            d = ItalianComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,
                             comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('italian')
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
                return redirect('/italianlogin')
            except IntegrityError:
                messages.warning(request,'This username already in use. Please choose another')
    context={'form':form}
    return render(request,'italian-store/auth/register.html',context)

def italiangetpatch(request):
    return render(request,'italian-store/getpatch.html')

def italianusepatch(request):
    return render(request,'italian-store/usepatch.html')