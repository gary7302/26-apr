from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

def tagaloghome(request):
    category=TagalogCategory.objects.all()
    return render(request,'tagalog-store/index.html',{'category':category})


def tagalogdetails(request):
    return render(request,'tagalog-store/details.html')

def tagalogcomment(request,id):
    eachProduct=TagalogCategory.objects.get(id=id)
    form=TagalogCommentForm()
    context={'form':form,'eachProduct':eachProduct}
    return render(request,'tagalog-store/coment.html',context)

@login_required(login_url='tagaloglogin')
def tagalogaddcomment(request,id):
    if request.method == "POST":
        form=TagalogCommentForm(request.POST,request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = TagalogCategory.objects.get(id=id)
            d = TagalogComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,
                             comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('tagalog')
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
                return redirect('/tagaloglogin')
            except IntegrityError:
                messages.warning(request,'This username altreay in use. Please choose another')
    context={'form':form}
    return render(request,'tagalog-store/auth/register.html',context)

def tagaloggetpatch(request):
    return render(request,'tagalog-store/getpatch.html')

def tagalogusepatch(request):
    return render(request,'tagalog-store/usepatch.html')