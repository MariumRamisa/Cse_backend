# Generated by Django 4.1.3 on 2022-12-09 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('burned_cal', '0001_initial'),
        ('user_calorie_details', '0006_remove_user_calorie_detail_remaining_calorie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_calorie_detail',
            name='burned_calorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='burned_cal.burned_cal_detail'),
        ),
    ]