from django.db import models
from students.models import *
from courses.models import *

# Create your models here.

STATUS = (
    ('Active', 'Active'),
    ('Completed', 'Completed')
)
 
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS)
    is_deleted = models.BooleanField(default=False,null=True)