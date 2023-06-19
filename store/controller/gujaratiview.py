from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from store.forms import *
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

def gujaratihome(request):
    category=GujaratiCategory.objects.all()
    return render(request,'gujarati-store/index.html',{'category':category})

def gujaraticomment(request,id):
    eachProduct = GujaratiCategory.objects.get(id=id)

    form = GujaratiCommentForm()
    context = {'form': form, 'eachProduct': eachProduct}
    return render(request, 'gujarati-store/coment.html', context)

@login_required(login_url='gujaratilogin')
def gujaratiaddcomment(request,id):
    if request.method == "POST":
        form = GujaratiCommentForm(request.POST, request.FILES)
        if form.is_valid():
            commenter_name = request.user
            comment_body = form.cleaned_data['comment_body']
            comment_image = form.cleaned_data['comment_image']
            eachProduct = GujaratiCategory.objects.get(id=id)
            d = GujaratiComment(product=eachProduct, commenter_name=commenter_name, comment_body=comment_body,comment_image=comment_image, created_at=datetime.now())
            d.save()
            return redirect('gujarati')
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
                return redirect('/gujaratilogin')
            except IntegrityError:
                messages.warning(request,'This username already in use. Please choose another')
    context={'form':form}
    return render(request,'gujarati-store/auth/register.html',context)

def gujaratidetails(request):
    return render(request,'gujarati-store/details.html')

def gujaratigetpatch(request):
    return render(request,'gujarati-store/getpatch.html')

def gujaratiusepatch(request):
    return render(request,'gujarati-store/usepatch.html')