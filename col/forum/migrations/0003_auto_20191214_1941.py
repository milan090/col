# Generated by Django 2.2.5 on 2019-12-14 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20191214_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='user',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
