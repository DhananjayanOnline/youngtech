# Generated by Django 2.2 on 2022-02-11 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=250)),
            ],
        ),
    ]
