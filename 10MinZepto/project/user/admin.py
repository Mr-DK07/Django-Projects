from django.contrib import admin
from . models import *


# Register your models here.

class contactAdmin(admin.ModelAdmin):
    list_display=('Name','Email','Mobile','Message')
admin.site.register(contact,contactAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cname', 'cpic', 'cdate')
admin.site.register(category,categoryAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display = ('id','spic', 'sdate')
admin.site.register(slider,sliderAdmin)

class subcategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name', 'subcategory_name')
admin.site.register(subcategory,subcategoryAdmin)

class productsAdmin(admin.ModelAdmin):
    list_display = ('id','product_category','subcategory_name','product_pic','price','discount_price','total_discount','product_quantity','pdate')
admin.site.register(products,productsAdmin)

class registerAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'mobile', 'passwd', 'address','profile')
admin.site.register(register,registerAdmin)

class cartAdmin(admin.ModelAdmin):
    list_display=('id','userid','product_name','quantity','price','total_price','product_picture','pw','added_date')
admin.site.register(cart,cartAdmin)

class myorderAdmin(admin.ModelAdmin):
    list_display=('id','userid','product_name','quantity','price','total_price','product_picture','pw','orderd_date','status')
admin.site.register(myorder,myorderAdmin)
    