from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from datetime import datetime
from django.db import connection

# Create your views here.

def index(request):
    data=category.objects.all().order_by('-id')
    sdata=slider.objects.all().order_by('-id')[0:3]
    pdata=products.objects.all().order_by('-id')[0:12]
    odata=products.objects.filter(total_discount__gte=20)[0:12]
    mdict={"cdata":data,"sdata":sdata,"pdata":pdata,"odata":odata}
    return render(request, 'user/index.html',mdict)


def aboutus(request):
    return render(request, 'user/aboutus.html')
def contactus(request):
    if request.method=="POST":
        a1=request.POST.get('name')
        a2=request.POST.get('email')
        a3=request.POST.get('mobile')
        a4=request.POST.get('message')
        #print(a1,a2,a3,a4)
        x=contact(Name=a1,Email=a2,Mobile=a3,Message=a4).save()
        print(x)
        return HttpResponse("<script>alert('Thankyou for contacting us...'); location.href='/user/contactus/' </script>")

    return render(request, 'user/contactus.html')

def signup(request):
    if request.method=='POST':
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        passwd=request.POST.get('passwd')
        address=request.POST.get('address')
        pic=request.FILES['fu']
        x=register.objects.all().filter(email=email).count()
        if(x==1):
            return HttpResponse("<script>alert('You are already registered...');location.href='/user/signup/'</script>")
        else:
            register(name=name,mobile=mobile,email=email,passwd=passwd,address=address,profile=pic).save()
            return HttpResponse("<script>alert('You are registered successfully...');location.href='/user/login/'</script>")
    return render(request, 'user/signup.html')


def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        passwd=request.POST.get('passwd')
        x=register.objects.filter(email=email,passwd=passwd).count()
        if x==1:
            y=register.objects.filter(email=email,passwd=passwd)
            request.session['user']=email
            request.session['username']=str(y[0].name)
            request.session['userpic']=str(y[0].profile)
            user=request.session.get('user')
            cartitems=cart.objects.filter(userid=user).count()
            request.session['cartitems']=cartitems
            return HttpResponse("<script>location.href='/user/index/'</script>")
        else:
            return HttpResponse("Username or password is incorrect.")
    return render(request, 'user/login.html')


def product(request):
    catid=request.GET.get('cid')
    subcatid=request.GET.get('sid')
    sdata=subcategory.objects.all().order_by('-id')
    
    if subcatid is not None:
        pdata=products.objects.all().filter(subcategory_name=subcatid)
    elif catid is not None:
        pdata=products.objects.all().filter(product_category=catid)
    else:
        pdata=products.objects.all().order_by('-id')
    md={"subcat":sdata,"pdata":pdata}

    return render(request, 'user/product.html',md)

def logout(request):
    if request.session.get('user'):
        del request.session['user']
        del request.session['userpic']
        return HttpResponse("<script>location.href='/user/index/'</script>")
    return render(request,'user/logout.html')

def profile(request):
    user=request.session.get('user')
    if request.method=='POST':
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        passwd=request.POST.get('passwd')
        address=request.POST.get('address')
        pic=request.FILES['fu']
        register(name=name,email=user,mobile=mobile,passwd=passwd,address=address,profile=pic).save()
        return HttpResponse("<script>alert('Your profile is updated successfully..');location.href='/user/profile/'</script>")
    rdata=""
    if user:
        rdata=register.objects.filter(email=user)   
    md={"rdata":rdata}
    return render(request,'user/profile.html',md)

def mycart(request):
    user=request.session.get('user')
    if user:
        qt=int(request.GET.get('qt'))
        pname=request.GET.get('pname')
        price=int(request.GET.get('price'))
        ppic=request.GET.get('ppic')
        pw=request.GET.get('pw')
        total_price=qt*price
        if qt>0:
            cart(userid=user,product_name=pname,quantity=qt,price=price,product_picture=ppic,pw=pw,total_price=total_price,added_date=datetime.now().date()).save()
            cartitems=cart.objects.filter(userid=user).count()
            request.session['cartitems']=cartitems
            return HttpResponse("<script>location.href='/user/products/'</script>")
        else:
            return HttpResponse("<script>alert('increase your cartitems...');location.href='/user/products/'</script>")   
    return render(request,'user/mycart.html')


def cartitems(request):
    user=request.session.get('user')
    cid=request.GET.get('cid')

    cartdata="";
    if user:
        cartdata=cart.objects.filter(userid=user)
        if cid is not None:
            cart.objects.filter(id=cid).delete()
            return HttpResponse("<script>alert('Your cart item is removed successfully');location.href='/user/cartitems/'</script>")
    md={"cartdata":cartdata}
    return render(request,'user/cartitems.html',md)


def morder(request):
    msg=request.GET.get('msg')
    user=request.session.get('user')
    if msg is not None:
        cursor=connection.cursor()
        cursor.execute("insert into user_myorder(product_name,quantity,price,total_price,product_picture,pw,userid,status,orderd_date) select product_name,quantity,price,total_price,product_picture,pw,'"+str(user)+"','Pending','"+str(datetime.now().date())+"' from user_cart where userid='"+str(user)+"'")
        cart.objects.filter(userid=user).delete()
        cartitems=cart.objects.filter(userid=user).count()
        request.session['cartitems']=cartitems
        return HttpResponse("<script>alert('Order Placed');location.href='/user/orderlist/'</script>")
           
    return render(request,'user/order.html')

def indexcart(request):
    user=request.session.get('user')
    if user:
        qt=int(request.GET.get('qt'))
        pname=request.GET.get('pname')
        price=int(request.GET.get('price'))
        ppic=request.GET.get('ppic')
        pw=request.GET.get('pw')
        total_price=qt*price
        if qt>0:
            cart(userid=user,product_name=pname,quantity=qt,price=price,product_picture=ppic,pw=pw,total_price=total_price,added_date=datetime.now().date()).save()
            cartitems=cart.objects.filter(userid=user).count()
            request.session['cartitems']=cartitems
            return HttpResponse("<script>location.href='/user/index/'</script>")
        else:
            return HttpResponse("<script>alert('increase your cartitems...');location.href='/user/index/'</script>")
    return render(request,'user/indexcart.html')



def adminprofile(request):
    return render(request,'user/adminprofile.html')

def orderlist(request):
    oid=request.GET.get('oid')
    user=request.session.get('user')
    pdata=myorder.objects.filter(userid=user,status="Pending")
    adata=myorder.objects.filter(userid=user,status="Accepted")
    ddata=myorder.objects.filter(userid=user,status="Delivered")
    if oid is not None:
        myorder.objects.filter(id=oid).delete()
        return HttpResponse("<script>location.href='/user/orderlist/'</script>")
    mydict={"pdata":pdata,"adata":adata,"ddata":ddata}
    return render(request,'user/orderlist.html',mydict)


