from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),

    path('home',views.home,name='home'),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('login2',views.login2,name="login2"),
    path('rcomplete',views.rcomplete,name="rcomplete"),
   
    path('lungcancer',views.lungcancer,name='lungcancer'),
   
    path('predict',views.predict,name='predict'),
    path('datafetch',views.datafetch,name="datafetch"),
   
    path('lungesv',views.lungesv,name='lungesv'),
   
]