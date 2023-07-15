# Generated by Django 4.2.2 on 2023-07-10 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0006_remove_maildata_choice_remove_maildata_mainmsg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='maildata',
            name='MailingCreationDate',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='maildata',
            name='MailingDeliveryDate',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='maildata',
            name='MailMessage',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='maildata',
            name='MailingAddress',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]