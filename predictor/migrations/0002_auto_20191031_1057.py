# Generated by Django 2.2 on 2019-10-31 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnover',
            name='Department',
            field=models.CharField(choices=[('Sales', 'Sales'), ('R & D', 'Research & Development'), ('H R', 'Human Resources')], default=0, max_length=100),
        ),
    ]