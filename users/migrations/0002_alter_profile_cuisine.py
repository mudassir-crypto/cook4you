# Generated by Django 3.2.7 on 2021-09-10 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cuisine',
            field=models.ManyToManyField(blank=True, to='users.Cuisine'),
        ),
    ]
