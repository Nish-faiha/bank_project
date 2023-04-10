# Generated by Django 3.2.18 on 2023-04-03 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankingapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('age', models.IntegerField(max_length=250)),
                ('gender', models.CharField(max_length=10)),
                ('phonenumber', models.IntegerField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=250)),
                ('district', models.CharField(max_length=250)),
                ('branch', models.CharField(max_length=250)),
                ('accounttype', models.CharField(max_length=250)),
                ('materialsprovide', models.CharField(max_length=250)),
            ],
        ),
    ]