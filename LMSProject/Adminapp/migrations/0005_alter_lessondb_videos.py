# Generated by Django 3.2.10 on 2023-08-13 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0004_cmodulesdb_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessondb',
            name='Videos',
            field=models.FileField(blank=True, max_length=250, null=True, upload_to='videos'),
        ),
    ]
