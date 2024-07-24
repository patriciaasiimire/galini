# Generated by Django 5.0.7 on 2024-07-23 17:46

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mental', '0004_remove_therapistprofile_email_alter_review_comment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(default='', max_length=250)),
                ('image', models.ImageField(upload_to='uploads/patient')),
            ],
        ),
        migrations.CreateModel(
            name='Therapist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('specialty', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('image', models.ImageField(upload_to='uploads/therapist')),
                ('bio', models.CharField(blank=True, default='', max_length=250, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='therapistprofile',
            name='user',
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(blank=True, default=datetime.datetime.today, null=True)),
                ('status', models.BooleanField(default=False)),
                ('patient', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mental.patient')),
                ('therapist', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mental.therapist')),
            ],
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='TherapistProfile',
        ),
    ]
