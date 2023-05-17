from django.shortcuts import render,redirect
from django.contrib import messages
from store.models import *
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

def addtocart(request):
    if request.method == "POST":
        if request.user.is_authenticated:

            product_id_str=request.POST.get('product_id')
            if product_id_str is not None:
                prod_id = int(product_id_str)
            else:
                return JsonResponse({'status': 'Product already in Cart'+str(product_id_str)})

            product_check=Product.objects.get(id=prod_id)
            if product_check:
                if(Cart.objects.filter(user_id=request.user.id,product_id=prod_id)):
                    return JsonResponse({'status':'Product already in Cart'})
                else:
                    prod_qty=int(request.POST.get('product_qty'))
                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(user=request.user,product_id=prod_id,quantity=prod_qty)
                        return JsonResponse({'status':"Product added successfully"})
                    else:
                        return JsonResponse({'status':'Only '+str(product_check.quantity)+' quantity available'})
            else:
                return JsonResponse({'status':'No such product found'})
        else:
            return JsonResponse({'status':'Login to Continue'})
    else:
        return redirect('/')
@login_required(login_url='loginpage')
def showCart(request):
    cart=Cart.objects.filter(user=request.user)
    context={'cart':cart}
    return render(request,'store/cart.html',context)
@csrf_exempt
def updatecart(request):
    if request.method == "POST":
        product_id_str = request.POST.get('product_id')
        if product_id_str is not None:
            prod_id = int(product_id_str)
        else:
            return JsonResponse({'status': 'Product already in Cart' + str(product_id_str)})

        if(Cart.objects.filter(user=request.user,product_id=prod_id)):
            prod_qty=request.POST.get('product_qty')
            cart=Cart.objects.get(user=request.user,product_id=prod_id)
            cart.quantity=prod_qty
            cart.save()
            return JsonResponse({'status':'Updated Successfully'})
    return redirect('/')

def deletecartitem(request):
    if request.method == "POST":
        prod_id=int(request.POST.get('product_id'))
        cartitem=Cart.objects.get(user=request.user,product_id=prod_id)
        cartitem.delete()
        return JsonResponse({'status':'Deleted Successfully'})
    return redirect('/')

@login_required(login_url='chineselogin')
def chinesecart(request):
    return render(request,'chinese-store/cart.html')

@login_required(login_url='hindilogin')
def hindicart(request):
    return render(request,'hindi-store/cart.html')

@login_required(login_url='spanishlogin')
def spanishcart(request):
    return render(request,'spanish-store/cart.html')

@login_required(login_url='frenchlogin')
def frenchcart(request):
    return render(request,'french-store/cart.html')

@login_required(login_url='arabiclogin')
def arabiccart(request):
    return render(request,'arabic-store/cart.html')

@login_required(login_url='bengalilogin')
def bengalicart(request):
    return render(request,'bengali-store/cart.html')

@login_required(login_url='russianlogin')
def russiancart(request):
    return render(request,'russian-store/cart.html')
