from django.db import models
from django.utils import timezone


# Create your models here.
class Turnover(models.Model):
    EDUCATION_CHOICES = [
        ('1', 1),
        ('1', 2),
        ('1', 3),
        ('1', 4),
        ('1', 5),
    ]
    DEPARTMENT_CHOICES = [
        ('Sales', 'Sales'),
        ('R & D', 'Research & Development'),
        ('H R', 'Human Resources'),
    ]
    ENVIRONMENT_SATISFACTION = [
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
    ]
    JOBINVOLVEMENT_CHOICES = [
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
    ]
    JOBLEVEL_CHOICES = [
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
    ]
    JOBSATISFACTION_CHOICES = [
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
    ]
    PERFORMANCE_RATING = [('3', 3), ('4', 4), ('5', 5)]
    STOCK_OPTION_CHOICES = [
        ('0', 0),
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
    ]
    BUSINESS_TRAVEL_CHOICES = [
        ("Rarely", "Travel_Rarely"),
        ("Frequently", "Travel_Frequently"),
        ("Non-Travel", "Non-Travel"),
    ]
    EDUCATION_FIELD = [('L S', 'Life Sciences'), ('Medical', 'Medical'),
                       ('Marketing', 'Marketing'), ('T D', 'Technical Degree'),
                       ('H R', 'Human Resources'), ('Other', 'Other')]
    JOB_ROLE_CHOICES = [
        ('S.E', 'Sales Executive'),
        ('R.S', 'Research Scientist'),
        ('L.T', 'Laboratory Technician'),
        ('M.D', 'Manufacturing Director'),
        ('H.R', 'Healthcare Representative'),
        ('Manager', 'Manager'),
        ('S.P', 'Sales Representative'),
        ('R.D', 'Research Director'),
        ('R.D', 'Research Director'),
        ('H.R', 'Human Resources'),
    ]

    Age = models.IntegerField(default=0)
    DistanceFromHome = models.CharField(max_length=100, default=0)
    Education = models.CharField(choices=EDUCATION_CHOICES,
                                 max_length=100,
                                 default=0)
    EnvironmentSatisfaction = models.CharField(
        max_length=100, choices=ENVIRONMENT_SATISFACTION, default=0)
    JobInvolvement = models.CharField(max_length=100,
                                      choices=JOBINVOLVEMENT_CHOICES,
                                      default=0)
    JobLevel = models.CharField(max_length=100,
                                choices=JOBLEVEL_CHOICES,
                                default=0)
    JobSatisfaction = models.CharField(max_length=100,
                                       choices=JOBSATISFACTION_CHOICES,
                                       default=0)
    MonthlyIncome = models.DecimalField(max_digits=10, decimal_places=2)
    NumCompaniesWorked = models.CharField(max_length=100, default=2)
    PercentSalaryHike = models.CharField(max_length=100, default=20)
    PerformanceRating = models.CharField(max_length=100,
                                         choices=PERFORMANCE_RATING,
                                         default=0)
    StockOptionLevel = models.CharField(max_length=100,
                                        choices=STOCK_OPTION_CHOICES,
                                        default=0)
    YearsSinceLastPromotion = models.CharField(max_length=100, default=2)
    BusinessTravel = models.CharField(max_length=100,
                                      choices=BUSINESS_TRAVEL_CHOICES,
                                      default=0)
    Department = models.CharField(max_length=100,
                                  choices=DEPARTMENT_CHOICES,
                                  default=0)

    TotalWorkingYears = models.CharField(max_length=100, default=2)
    YearsAtCompany = models.CharField(max_length=100, default=2)
    YearsInCurrentRole = models.CharField(max_length=100, default=2)
    EducationField = models.CharField(max_length=100,
                                      choices=EDUCATION_FIELD,
                                      default='Medical')
    JobRole = models.CharField(max_length=100, choices=JOB_ROLE_CHOICES)


    def __str__(self):
        return self.Education
