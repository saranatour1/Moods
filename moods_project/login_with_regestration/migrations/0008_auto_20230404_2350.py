# Generated by Django 2.2.4 on 2023-04-04 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_with_regestration', '0007_request'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='request',
            unique_together={('request_sender', 'request_reciever')},
        ),
    ]