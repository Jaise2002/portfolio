# Generated by Django 5.0.1 on 2024-02-14 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20240204_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark1', models.TextField(max_length=20)),
                ('mark2', models.TextField(max_length=20)),
                ('mark3', models.TextField(max_length=20)),
                ('mark4', models.TextField(max_length=20)),
            ],
        ),
    ]
