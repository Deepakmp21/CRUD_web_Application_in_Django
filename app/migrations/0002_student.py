# Generated by Django 4.2 on 2023-04-20 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Contact', models.IntegerField()),
            ],
        ),
    ]
