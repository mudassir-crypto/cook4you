# Generated by Django 3.2.7 on 2021-09-16 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='experience',
            name='employment_type',
            field=models.CharField(blank=True, choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Self Employed', 'Self Employed'), ('Internship', 'Internship'), ('Trainee', 'Trainee')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
