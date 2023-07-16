from django.shortcuts import render , redirect
from django.views.generic.edit import FormView
from .models import MailData
from django.http import HttpResponse
from datetime import datetime , timedelta
import calendar
import time

from .AutoMail import auto_func


def home_page_view(request):
    return render(request , 'MailForm.html')

def About_view(request):
    return render(request , 'About.html')

def FAQ_view(request):
    return render(request , 'HowItWorks.html')

def activate_script_view(request):
    auto_func()
    return HttpResponse("Mail Automation Script Activated.You may exit now.")


def MailData_Register(request):
    if request.method == 'POST':
        user_text = request.POST.get('UserText1')
        user_email = request.POST.get('Useremail1')
        mail_creation_date = datetime.now().date()
        mail_creation_date_only = mail_creation_date.strftime('%Y-%m-%d')
        user_choice = request.POST.get('option')    
        if user_choice == '1DAY':   
            mail_deliver_date = mail_creation_date + timedelta(days=1)
            mail_deliver_date_only =  mail_deliver_date.strftime('%Y-%m-%d')
        elif user_choice == '1WEEK':   
            mail_deliver_date = mail_creation_date + timedelta(days=7)
            mail_deliver_date_only =  mail_deliver_date.strftime('%Y-%m-%d')
        elif user_choice == '1MONTH':  
            _, num_days = calendar.monthrange(mail_creation_date.year, mail_creation_date.month)
            mail_deliver_date = mail_creation_date + timedelta(days=num_days)    
            mail_deliver_date_only =  mail_deliver_date.strftime('%Y-%m-%d')
        elif user_choice == '1YEAR':   
            current_year = datetime.now().year
            if calendar.isleap(current_year):
             mail_deliver_date = mail_creation_date + timedelta(days = 366)
            else:
             mail_deliver_date = mail_creation_date + timedelta(days = 365)
             mail_deliver_date_only =  mail_deliver_date.strftime('%Y-%m-%d')
        elif user_choice == '5YEARS':   
            mail_deliver_date = mail_creation_date + timedelta(days=1825)
            mail_deliver_date_only =  mail_deliver_date.strftime('%Y-%m-%d')
        else:
            mail_deliver_date = mail_creation_date + timedelta(days=3652)
            mail_deliver_date_only =  mail_deliver_date.strftime('%Y-%m-%d')
        #response_content = f'Mail Creation Successfull {user_text} , {user_email} , {mail_creation_date_only} , {mail_deliver_date_only} '
        Obj = MailData(MailMessage = user_text , MailingAddress = user_email , MailingCreationDate = mail_creation_date_only , MailingDeliveryDate= mail_deliver_date_only , MailStatus=False)
        Obj.save()
        context ={
            'Obj' : Obj
        }
    time.sleep(2)
    return render(request, 'success.html' , context)