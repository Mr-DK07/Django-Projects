from re import A
from django.shortcuts import render
from django.http import HttpResponse
from . models import *

# Create your views here.
def index(request):
    edata=explore.objects.all().order_by('-id')[0:6]
    pdata=property.objects.all().order_by('-id')[0:8]
    etdata=easytrip.objects.all().order_by('-id')
    ntdata=nexttrip.objects.all().order_by('-id')[2:4]
    updata=uniprop.objects.all().order_by('-id')[2:7]
    hgdata=homeguest.objects.all().order_by('-id')[0:4]
    dict={"edata":edata,"pdata":pdata,"etdata":etdata,"ntdata":ntdata,"updata":updata,"hgdata":hgdata}
    return render(request, 'user/index.html',dict)

def aboutus(request):
    return render(request, 'user/aboutus.html')

def contactus(request):
    if request.method=="POST":
        a1=request.POST.get('name')
        a2=request.POST.get('mobile')
        a3=request.POST.get('message')
        x=contact(Name=a1,Mobile=a2,Message=a3).save()
        print(x)
        return HttpResponse("<script>alert('Thankyou for contacting us...'); location.href='/user/contactus/' </script>")
    return render(request, 'user/contactus.html')

def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        x=register.objects.filter(email=email,password=password).count()
        if x==1:
            y=register.objects.filter(email=email,password=password)
            request.session['user']=email
            request.session['username']=str(y[0].name)
            request.session['userpic']=str(y[0].profile)
            user=request.session.get('user')
            return HttpResponse("<script>location.href='/user/index/'</script>")
        else:
            return HttpResponse("Username or password is incorrect.")
    return render(request, 'user/login.html')

def signup(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        pic=request.FILES['profile']
        x=register.objects.all().filter(email=email).count()
        if(x==1):
            return HttpResponse("<script>alert('You are already registered...');location.href='/user/signup/'</script>")
        else:
            register(name=name,email=email,password=password,profile=pic).save()
            return HttpResponse("<script>alert('You are registered successfully...');location.href='/user/login/'</script>")
    return render(request, 'user/signup.html')

def logout(request):
    if request.session.get('user'):
        del request.session['user']
        del request.session['username']
        del request.session['userpic']
        return HttpResponse("<script>location.href='/user/index/'</script>")
    return render(request,'user/logout.html')

def account(request):
    user=request.session.get('user')
    if request.method=='POST':
        name=request.POST.get('name')
        password=request.POST.get('password')
        pic=request.FILES['profile']
        register(name=name,email=user,password=password,profile=pic).save()
        return HttpResponse("<script>alert('Your profile is updated successfully..');location.href='/user/useraccount/'</script>")
    rdata=""
    if user:
        rdata=register.objects.filter(email=user)  
    md={"rdata":rdata}
    return render(request, 'user/useraccount.html',md)

def Hotels(request):
    hotelsData=hotels.objects.all().order_by('-id')
    hotelsDict={"hotelsData":hotelsData}
    return render(request, 'user/hotels.html',hotelsDict)


def team(request):
    return render(request, 'user/team.html')

def Hotel(request):
    hotelData=hotel.objects.all().order_by('-id')
    hotelsData=hotels.objects.all().order_by('-id')
    hotelDict={"hotelData":hotelData,"hotelsData":hotelsData}
    return render(request, 'user/hotel.html',hotelDict)

def userdetails(request):
    if request.method=="POST":
        firstName=request.POST.get('firstName')
        lastName=request.POST.get('lastName')
        countryName=request.POST.get('countryName')
        email=request.POST.get('email')
        fullGuestName=request.POST.get('fullGuestName')
        mobile=request.POST.get('mobile')
        address=request.POST.get('address')
        details=userDetails(firstName=firstName,lastName=lastName,countryName=countryName,fullGuestName=fullGuestName,mobile=mobile,address=address,email=email).save()
        print(details)
        return HttpResponse("<script>location.href='/user/payment/' </script>")   
    return render(request, 'user/userdetails.html')


def payment(request):
    user=request.session.get('user')
    if request.method=="POST":
        cardHolderName=request.POST.get('cardHolderName')
        cardType=request.POST.get('cardType')
        cardNumber=request.POST.get('cardNumber')
        expirationDate=request.POST.get('expirationDate')
        
        #cvvNum=request.POST.get('cvvNum')
        # OTP=request.POST.get('OTP')
        paymentd=paymentDetails(cardHolderName=cardHolderName,cardType=cardType,cardNumber=cardNumber,expirationDate=expirationDate).save()
        print(paymentd)
        if user:
            x=register.objects.filter(email=user)
            return HttpResponse("<script> alert('Your hotel is booked successfully.');location.href='/user/index/' </script>")
        else:
            return HttpResponse("<script>alert('Please login first...');location.href='/user/login/'</script>")
    return render(request, 'user/payment.html')

