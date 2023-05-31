from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

def frenchhome(request):
    category=FrenchCategory.objects.all()
    return render(request,'french-store/index.html',{'category':category})

def frenchcomment(request,id):
    eachProduct = FrenchCategory.objects.get(id=id)

    form = FrenchCommentForm()
    context = {'form': form, 'eachProduct': eachProduct}
    return render(request, 'french-store/coment.html', context)

@login_required(login_url='frenchlogin')
def frenchaddcomment(request,id):
    if request.method == "POST":
        form = FrenchCommentForm(request.POST, request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = FrenchCategory.objects.get(id=id)
            d = FrenchComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('french')
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
                return redirect('/frenchlogin')
            except IntegrityError:
                messages.warning(request,'This username already in use. Please choose another')
    context={'form':form}
    return render(request,'french-store/auth/register.html',context)

def frenchdetails(request):
    return render(request,'french-store/details.html')

def frenchgetpatch(request):
    return render(request,'french-store/getpatch.html')

def frenchusepatch(request):
    return render(request,'french-store/usepatch.html')