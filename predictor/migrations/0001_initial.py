# Generated by Django 2.2 on 2019-10-30 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turnover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age', models.IntegerField(default=0)),
                ('DistanceFromHome', models.CharField(default=0, max_length=100)),
                ('Education', models.CharField(choices=[('1', 1), ('1', 2), ('1', 3), ('1', 4), ('1', 5)], default=0, max_length=100)),
                ('EnvironmentSatisfaction', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4)], default=0, max_length=100)),
                ('JobInvolvement', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4)], default=0, max_length=100)),
                ('JobLevel', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default=0, max_length=100)),
                ('JobSatisfaction', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4)], default=0, max_length=100)),
                ('MonthlyIncome', models.DecimalField(decimal_places=2, max_digits=10)),
                ('NumCompaniesWorked', models.CharField(default=2, max_length=100)),
                ('PercentSalaryHike', models.CharField(default=20, max_length=100)),
                ('PerformanceRating', models.CharField(choices=[('3', 3), ('4', 4), ('5', 5)], default=0, max_length=100)),
                ('StockOptionLevel', models.CharField(choices=[('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4)], default=0, max_length=100)),
                ('YearsSinceLastPromotion', models.CharField(default=2, max_length=100)),
                ('BusinessTravel', models.CharField(choices=[('Rarely', 'Travel_Rarely'), ('Frequently', 'Travel_Frequently'), ('Non-Travel', 'Non-Travel')], default=0, max_length=100)),
                ('Department', models.CharField(default=0, max_length=100)),
            ],
        ),
    ]