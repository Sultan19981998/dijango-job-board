# Generated by Django 5.2 on 2025-05-27 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_apply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='creat_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
