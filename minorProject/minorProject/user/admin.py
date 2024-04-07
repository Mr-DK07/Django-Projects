from django.contrib import admin
from . models import *

# Register your models here.

class exploreAdmin(admin.ModelAdmin):
    list_display = ('id','epic', 'ename','eno',  'edate')
admin.site.register(explore,exploreAdmin)

class propertyAdmin(admin.ModelAdmin):
    list_display = ('id','ppic', 'pname', 'pdate')
admin.site.register(property,propertyAdmin)

class easytripAdmin(admin.ModelAdmin):
    list_display = ('id','etpic', 'etname','etdis',  'etdate')
admin.site.register(easytrip,easytripAdmin)

class nexttripAdmin(admin.ModelAdmin):
    list_display = ('id','ntpic','ntname','ntabout','ntdate')
admin.site.register(nexttrip,nexttripAdmin)

class unipropAdmin(admin.ModelAdmin):
    list_display = ('id','uppic','upname','uplocation','uprating','upreviews','update')
admin.site.register(uniprop,unipropAdmin)


class homeguestAdmin(admin.ModelAdmin):
    list_display = ('id','hgpic','hgname','hglocation','hgrating','hgreviews','hgprice','hgdate')
admin.site.register(homeguest,homeguestAdmin)

class contactAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Mobile', 'Message')
admin.site.register(contact,contactAdmin)

class registerAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'password','profile')
admin.site.register(register,registerAdmin)

class hotelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'Destination', 'hotelName', 'hotelPicture', 'hotelLocation', 'hotelDescription', 'hotelPrice', 'hotelGrade', 'hotelRating', 'hotelReviews')
admin.site.register(hotels,hotelsAdmin)

class hotelAdmin(admin.ModelAdmin):
    list_display = ('id','hotelName','Destination','hotelPicture','hotelLocation','hotelDescription','hotelPicture1', 'hotelPicture2', 'hotelPicture3', 'hotelPicture4', 'hotelPicture5', 'hotelPicture6')
admin.site.register(hotel,hotelAdmin)

class userDetailsAdmin(admin.ModelAdmin):
    list_display = ('id','firstName','lastName','countryName','email','fullGuestName','mobile', 'address')
admin.site.register(userDetails,userDetailsAdmin)

class paymentDetailsAdmin(admin.ModelAdmin):
    list_display = ('id','cardHolderName','cardType','cardNumber','expirationDate','cvvNum','OTP')
admin.site.register(paymentDetails,paymentDetailsAdmin)