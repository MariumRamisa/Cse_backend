# Generated by Django 4.1.3 on 2022-12-09 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_details', '0009_remove_user_details_goal_user_details_goal_weight'),
        ('user_calorie_details', '0007_alter_user_calorie_detail_burned_calorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_calorie_detail',
            name='goal_calorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_details.user_details'),
        ),
    ]
