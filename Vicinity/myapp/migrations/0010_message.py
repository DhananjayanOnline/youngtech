# Generated by Django 4.0.3 on 2022-04-05 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_rename_creatorid_vote_uid_remove_post_downvotestatus_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('messageid', models.IntegerField(primary_key=True, serialize=False)),
                ('uid', models.IntegerField()),
                ('message', models.CharField(max_length=300)),
            ],
        ),
    ]
