# Generated by Django 4.2.2 on 2023-07-08 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0002_alter_maildata_choice_alter_maildata_mailingaddress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maildata',
            name='PresentDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]