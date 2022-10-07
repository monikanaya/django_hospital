from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
   path('',views.home,name='home'),
   
   
   path('details',views.deatils,name="deatail"),

   path('signup',views.signup,name="signup"),
   path('signin',views.signup,name="signin"),
   path('signout',views.signup,name="signout")
]
