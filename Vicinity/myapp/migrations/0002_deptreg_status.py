# Generated by Django 4.0.3 on 2022-03-08 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deptreg',
            name='status',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
