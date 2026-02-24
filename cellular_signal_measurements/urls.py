"""
URL configuration for cellular_signal_measurements project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views
from cellular_signal_measurements import views as mainView
from admins import views as admins
from users import views as usr
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),

    path("", mainView.index, name="index"),
    path("index", mainView.index, name="index"),
    path("Adminlogin", mainView.AdminLogin, name="AdminLogin"),
    path("UserLogin", mainView.UserLogin, name="UserLogin"),

    # admin views
    path("AdminLogincheck", admins.AdminLoginCheck, name="AdminLoginCheck"),
    path('userDetails', admins.RegisterUsersView, name='RegisterUsersView'),
    path('ActivUsers/', admins.ActivaUsers, name='activate_users'),
    path('DeleteUsers/', admins.DeleteUsers, name='delete_users'),
    path('adminhome', admins.adminhome, name='adminhome'),
    
    #userurls
    path("ViewDataset/", usr.ViewDataset, name="ViewDataset"),
    path('UserRegisterForm',usr.UserRegisterActions,name='UserRegisterForm'),
    path("UserLoginCheck/", usr.UserLoginCheck, name="UserLoginCheck"),
    path("UserHome/", usr.UserHome, name="UserHome"),
    path("index/", usr.index, name="index"),

    path('train_model/', views.train_model, name='train_model'),
    path('predict/', views.predict_signal, name='predict'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
