from operator import truediv
from django.db import models

# Create your models here.

class explore(models.Model):
    epic=models.ImageField(upload_to='static/explorepic/',null=True)
    ename=models.CharField(max_length=200,null=True)
    eno=models.CharField(max_length=100,null=True)
    edate=models.DateField()
    def __str__(self):
        return self.ename
    
class property(models.Model):
    ppic=models.ImageField(upload_to='static/propertypic/',null=True)
    pname=models.CharField(max_length=200,null=True)
    pdate=models.DateField()
    def __str__(self):
        return self.pname

class easytrip(models.Model):
    etpic=models.ImageField(upload_to='static/easytrippic/',null=True)
    etname=models.CharField(max_length=200,null=True)
    etdis=models.CharField(max_length=100,null=True)
    etdate=models.DateField()
    def __str__(self):
        return self.etname
    
class nexttrip(models.Model):
    ntpic=models.ImageField(upload_to= 'static/nexttrippic',null=True)
    ntname=models.CharField(max_length=200,null=True)
    ntabout=models.CharField(max_length=500,null=True)
    ntdate=models.DateField()
    def __str__(self):
        return self.ntname
    
class uniprop(models.Model):
    uppic=models.ImageField(upload_to= 'static/upropic',null=True)
    upname=models.CharField(max_length=200,null=True)
    uplocation=models.CharField(max_length=500,null=True)
    uprating=models.FloatField(max_length=20,null=True)
    upreviews=models.CharField(max_length=200,null=True)
    update=models.DateField()
    def __str__(self):
        return self.upname

class homeguest(models.Model):
    hgpic=models.ImageField(upload_to= 'static/homeguestpic',null=True)
    hgname=models.CharField(max_length=200,null=True)
    hglocation=models.CharField(max_length=500,null=True)
    hgrating=models.FloatField(max_length=20,null=True)
    hgreviews=models.CharField(max_length=200,null=True)
    hgprice=models.CharField(max_length=100,null=True)
    hgdate=models.DateField()
    def __str__(self):
        return self.hgname
    
class contact(models.Model):
    Name=models.CharField(max_length=200,null=True)
    Mobile=models.IntegerField(null=True)
    Message=models.TextField(null=True)
    def __str__(self):
        return self.Name
    
class register(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    profile=models.ImageField(upload_to='static/userpic/',null=True)
    
class hotels(models.Model):
    Destination=models.CharField(max_length=100,null=True)
    hotelName=models.CharField(max_length=500,null=True)
    hotelPicture=models.ImageField(upload_to='static/hotelspic/',null=True)  
    hotelLocation=models.CharField(max_length=500,null=True)
    hotelDescription=models.TextField(null=True)
    hotelPrice=models.CharField(max_length=100,null=True)
    hotelGrade=models.CharField(max_length=100,null=True)
    hotelRating=models.FloatField(max_length=15,null=True)
    hotelReviews=models.IntegerField(null=True)
    def __str__(self):
        return self.hotelName
    
class hotel(models.Model):
    hotelName=models.ForeignKey(hotels,on_delete=models.CASCADE)
    Destination=models.CharField(max_length=100,null=True)
    hotelPicture=models.ImageField(upload_to='static/hotelspic/',null=True) 
    hotelLocation=models.CharField(max_length=500,null=True)
    hotelDescription=models.TextField(null=True)
    hotelPicture1=models.ImageField(upload_to='static/hotelspic/',null=True)
    hotelPicture2=models.ImageField(upload_to='static/hotelspic/',null=True)
    hotelPicture3=models.ImageField(upload_to='static/hotelspic/',null=True)
    hotelPicture4=models.ImageField(upload_to='static/hotelspic/',null=True)
    hotelPicture5=models.ImageField(upload_to='static/hotelspic/',null=True)
    hotelPicture6=models.ImageField(upload_to='static/hotelspic/',null=True)
    def __str__(self):
        return self.hotelName
    
class userDetails(models.Model):
    firstName=models.CharField(max_length=100,null=True)
    lastName=models.CharField(max_length=100,null=True)
    countryName=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    fullGuestName=models.CharField(max_length=100,null=True)
    mobile=models.IntegerField(null=True)
    address=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.email

class paymentDetails(models.Model):
    cardHolderName=models.CharField(max_length=100,null=True)
    cardType=models.CharField(max_length=100,null=True)
    cardNumber=models.IntegerField(null=True)
    expirationDate=models.DateField(null=True)
    cvvNum=models.IntegerField(null=True)
    OTP=models.IntegerField(null=True)
    def __str__(self):
        return self.cardHolderName
    