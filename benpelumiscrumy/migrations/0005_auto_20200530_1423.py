# Generated by Django 3.0.6 on 2020-05-30 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('benpelumiscrumy', '0004_auto_20200528_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrumygoals',
            name='goal_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='scrumy_goal', to='benpelumiscrumy.GoalStatus'),
        ),
    ]
