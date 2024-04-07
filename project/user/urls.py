from django.urls import path
from . import views

urlpatterns=[
    path('index/',views.index),
    path('',views.index),
    path('aboutus/',views.aboutus),
    path('contactus/',views.contactus),
    path('signup/',views.signup),
    path('login/',views.login),
    path('products/',views.product),
    path('logout/',views.logout),
    path('profile/',views.profile),
    path('mycart/',views.mycart),
    path('cartitems/',views.cartitems),
    path('order/',views.morder),
    path('indexcart/',views.indexcart),
    path('adminprofile/',views.adminprofile),
    path('orderlist/',views.orderlist),
    
]