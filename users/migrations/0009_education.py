# Generated by Django 3.2.7 on 2021-09-18 09:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_profile_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('schoolName', models.CharField(blank=True, max_length=200, null=True)),
                ('degree', models.CharField(blank=True, max_length=200, null=True)),
                ('field_of_study', models.CharField(blank=True, max_length=400, null=True)),
                ('location', models.CharField(blank=True, max_length=400, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('grade', models.CharField(blank=True, max_length=12, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]