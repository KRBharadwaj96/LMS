# Generated by Django 3.2.10 on 2023-07-25 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ModName', models.CharField(blank=True, max_length=200, null=True)),
                ('LessonName', models.CharField(blank=True, max_length=200, null=True)),
                ('Videos', models.FileField(max_length=250, upload_to='videos')),
                ('Attendance', models.FileField(blank=True, null=True, upload_to='Attendance')),
            ],
        ),
    ]
