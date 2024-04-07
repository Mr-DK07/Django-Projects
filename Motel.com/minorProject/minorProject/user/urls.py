from django.urls import path
from . import views

urlpatterns=[
    path('index/',views.index),
    path('',views.index),
    path('aboutus/',views.aboutus),
    path('contactus/',views.contactus),
    path('login/',views.login),
    path('logout/',views.logout),
    path('signup/',views.signup),
    path('hotels/',views.Hotels),
    path('useraccount/',views.account),
    path('team/',views.team),
    path('hotel/',views.Hotel),
    path('userdetails/',views.userdetails),
    path('payment/',views.payment),

]