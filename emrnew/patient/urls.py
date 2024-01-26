from django.urls import path

from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('register',views.register,name="register"),
    path('login2',views.login2,name="login2"),
    path('pregister',views.pregister,name='pregister'),
    path('login',views.login,name='login'),
    path('LunCancerreport',views.LunCancerreport,name="LunCancerreport"),
    
]