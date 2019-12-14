# Generated by Django 2.2.5 on 2019-12-14 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='fk_question',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='fk_answered_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='fk_created_user',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='question',
            name='description',
        ),
        migrations.RemoveField(
            model_name='question',
            name='images',
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.TextField(),
        ),
    ]
