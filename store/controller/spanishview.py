from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

def spanishhome(request):
    category=SpanishCategory.objects.all()
    return render(request,'spanish-store/index.html',{'category':category})


def spanishdetails(request):
    return render(request,'spanish-store/details.html')


def spanishcomment(request,id):
    eachProduct=SpanishCategory.objects.get(id=id)
    form=SpanishCommentForm()
    context={'form':form,'eachProduct':eachProduct}
    return render(request,'spanish-store/coment.html',context)

@login_required(login_url='spanishlogin')
def spanishaddcomment(request,id):
    if request.method == "POST":
        form=SpanishCommentForm(request.POST,request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = SpanishCategory.objects.get(id=id)
            d = SpanishComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,
                             comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('spanish')
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
                return redirect('/spanishlogin')
            except IntegrityError:
                messages.warning(request,'This username altreay in use. Please choose another')
    context={'form':form}
    return render(request,'spanish-store/auth/register.html',context)

def spanishgetpatch(request):
    return render(request,'spanish-store/getpatch.html')

def spanishusepatch(request):
    return render(request,'spanish-store/usepatch.html')