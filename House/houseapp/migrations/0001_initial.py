# Generated by Django 2.2 on 2022-02-11 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HouseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('housename', models.CharField(max_length=250)),
                ('housenumber', models.IntegerField(max_length=20)),
            ],
        ),
    ]