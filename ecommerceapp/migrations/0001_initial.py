# Generated by Django 4.2.6 on 2023-12-10 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('desc', models.TextField(max_length=500)),
                ('phonenumber', models.IntegerField()),
            ],
        ),
    ]
