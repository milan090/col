# Generated by Django 2.2 on 2019-12-18 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_userprofileinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='portfolio_site',
        ),
    ]
