# Generated by Django 3.0.6 on 2020-06-03 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benpelumiscrumy', '0007_auto_20200603_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrumygoals',
            name='goal_id',
            field=models.IntegerField(default=6181, null=True, unique=True),
        ),
    ]
