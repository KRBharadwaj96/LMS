# Generated by Django 3.2.10 on 2023-08-11 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0003_auto_20230805_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmodulesdb',
            name='Subject',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
