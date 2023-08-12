# Generated by Django 3.1.4 on 2023-08-12 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scooters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('20 MPH SCOOTERS', '20 MPH SCOOTERS'), ('30 MPH SCOOTERS', '30 MPH SCOOTERS'), ('40 MPH SCOOTERS', '40 MPH SCOOTERS'), ('50 MPH SCOOTERS', '50 MPH SCOOTERS')], max_length=15)),
                ('brand', models.CharField(max_length=25)),
                ('model', models.CharField(max_length=25)),
                ('image', models.ImageField(upload_to='motorbikes_images')),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
