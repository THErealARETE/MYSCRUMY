# Generated by Django 3.0.6 on 2020-06-03 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benpelumiscrumy', '0006_auto_20200530_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrumygoals',
            name='goal_id',
            field=models.IntegerField(default=7090, unique=True),
        ),
    ]
