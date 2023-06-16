from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

def koreanhome(request):
    category=KoreanCategory.objects.all()
    return render(request,'korean-store/index.html',{'category':category})


def koreandetails(request):
    return render(request,'korean-store/details.html')

def koreancomment(request,id):
    eachProduct=KoreanCategory.objects.get(id=id)
    form=KoreanCommentForm()
    context={'form':form,'eachProduct':eachProduct}
    return render(request,'korean-store/coment.html',context)

@login_required(login_url='koreanlogin')
def koreanaddcomment(request,id):
    if request.method == "POST":
        form=KoreanCommentForm(request.POST,request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = KoreanCategory.objects.get(id=id)
            d = KoreanComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,
                             comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('korean')
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
                return redirect('/koreanlogin')
            except IntegrityError:
                messages.warning(request,'This username already in use. Please choose another')
    context={'form':form}
    return render(request,'korean-store/auth/register.html',context)

def koreangetpatch(request):
    return render(request,'korean-store/getpatch.html')

def koreanusepatch(request):
    return render(request,'korean-store/usepatch.html')