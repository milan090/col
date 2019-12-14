# Generated by Django 2.2.5 on 2019-11-22 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_auto_20191122_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercourses',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Course', unique=True),
        ),
        migrations.AlterField(
            model_name='usercourses',
            name='course_progress',
            field=models.IntegerField(default=0),
        ),
    ]
