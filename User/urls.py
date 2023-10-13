from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="Home"),
    path('register',views.register,name='Register'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
   






]