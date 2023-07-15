from django.db import models

class MailData(models.Model):
    MailMessage = models.TextField(max_length=10000 , null=True)
    MailingAddress = models.EmailField(null=True)
    MailingCreationDate = models.CharField(max_length=50 , null = True)
    MailingDeliveryDate = models.CharField(max_length=50 , null=True)
    MailStatus = models.BooleanField(null=True)

    def __str__(self):
        return self.MailingAddress


