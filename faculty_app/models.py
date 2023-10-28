from django.db import models
from django.contrib.auth.models import User
import datetime

DEPARTMENTS = [
    ('MCA', 'Computer Application'),
    ('MBA', 'Business Administration'),
    ('BHM', 'Hotel Management'),
    ('MCOM', 'Commerce'),
]

SUBJECTS = [
    ('COA', 'Computer Architecture and Analysis'),
    ('AOP', 'Art of Programming'),
    ('RM', 'Research Methodology'),
    ('BA', 'Business administration'),
    ('HM', 'Hotel Management'),
    ('MH', 'Management Hotel'),
    ('AC', 'Accounting'),
    ('CO', 'Commerce'),

]

class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='faculty')
    dob = models.DateField()
    department = models.CharField(max_length=4, choices=DEPARTMENTS)
    date_of_join = models.DateField()
    subject = models.CharField(max_length=4, choices=SUBJECTS)
    emp_id = models.CharField(max_length=10, unique=True)
    


    def __str__(self):
        return self.user.username



class Leave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(max_length=255)
    status = models.CharField(max_length=40, default='approval pending')

    def __str__(self):
        return self.user.username

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mark_date = models.DateField()
    mark_time = models.TimeField(default=datetime.time(0, 0))
    status = models.BooleanField(default=False)
