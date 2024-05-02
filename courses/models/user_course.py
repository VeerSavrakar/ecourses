from django.db import models
from django.contrib.auth.models import User
from courses.models import Course
from django.conf import settings

class UserCourse(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,null=False,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,null=False,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.user.username}-{self.course.name}'