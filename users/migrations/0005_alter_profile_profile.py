# Generated by Django 3.2.6 on 2021-09-10 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile',
            field=models.ImageField(blank=True, default='profiles/default.png', null=True, upload_to='profiles'),
        ),
    ]
