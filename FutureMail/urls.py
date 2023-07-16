"""
URL configuration for FutureMail project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Data.views import  MailData_Register , home_page_view ,activate_script_view , About_view , FAQ_view

urlpatterns = [
    path('xyz/', admin.site.urls),
    path('SendMail/' , MailData_Register , name="MailRegister"),
    path('' , home_page_view , name = "MailData"),
    path('activate/' , activate_script_view),
    path('About/' , About_view, name = "About"),
    path('HowitWorks/' , FAQ_view , name = "FAQ")
]
