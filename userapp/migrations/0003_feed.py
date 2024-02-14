# Generated by Django 5.0.1 on 2024-02-06 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_logintb'),
    ]

    operations = [
        migrations.CreateModel(
            name='feed',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
    ]
