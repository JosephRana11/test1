from .models import MailData
from datetime import datetime 
from django.conf import settings
from django.core.mail import send_mail
                                              
def auto_func():
    datetoday = datetime.now().date()
    datetodayonly = datetoday.strftime('%Y-%m-%d')
    query = MailData.objects.filter(MailStatus=False)
    try:
     for item in query:
        if datetodayonly == item.MailingDeliveryDate:
            subject = f"MAIL FROM:{item.MailingCreationDate}"
            message = item.MailMessage
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [item.MailingAddress, ]
            send_mail( subject, message, email_from, recipient_list )
            item.MailStatus = False
            item.save()
    except:
        pass
    