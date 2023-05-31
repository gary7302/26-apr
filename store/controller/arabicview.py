from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

def arabichome(request):
    category=ArabicCategory.objects.all()
    return render(request,'arabic-store/index.html',{'category':category})

def arabiccomment(request,id):
    eachProduct = ArabicCategory.objects.get(id=id)

    form = ArabicCommentForm()
    context = {'form': form, 'eachProduct': eachProduct}
    return render(request, 'arabic-store/coment.html', context)

@login_required(login_url='arabiclogin')
def arabicaddcomment(request,id):
    if request.method == "POST":
        form = ArabicCommentForm(request.POST, request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = ArabicCategory.objects.get(id=id)
            d = ArabicComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('arabic')
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
                return redirect('/arabiclogin')
            except IntegrityError:
                messages.warning(request,'This username already in use. Please choose another')
    context={'form':form}
    return render(request,'arabic-store/auth/register.html',context)

def arabicdetails(request):
    return render(request,'arabic-store/details.html')

def arabicgetpatch(request):
    return render(request,'arabic-store/getpatch.html')

def arabicusepatch(request):
    return render(request,'arabic-store/usepatch.html')