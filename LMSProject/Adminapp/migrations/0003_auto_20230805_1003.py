# Generated by Django 3.2.10 on 2023-08-05 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0002_lessondb'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmodulesdb',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='module'),
        ),
        migrations.AddField(
            model_name='lessondb',
            name='LImage',
            field=models.ImageField(blank=True, null=True, upload_to='Lesson'),
        ),
    ]
