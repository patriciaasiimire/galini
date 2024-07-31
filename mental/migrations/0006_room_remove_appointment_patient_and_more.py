# Generated by Django 5.0.7 on 2024-07-26 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mental', '0005_patient_therapist_remove_therapistprofile_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='therapist',
        ),
        migrations.AlterField(
            model_name='therapist',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]