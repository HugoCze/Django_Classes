# Generated by Django 3.2.5 on 2022-08-24 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=64)),
                ('LastName', models.CharField(max_length=64)),
                ('Email', models.CharField(max_length=128, unique=True)),
            ],
        ),
    ]
