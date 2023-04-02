from django.db import models
from user.models import Users
# Create your models here.

class Tracker(models.Model):
    cateory_choices=(('선택',None),('SHOP','쇼핑'),('EAT','식비'),
                     ('FIX','고정비'),('ACT','여가활동비'),
                     ('EDU','교육비'),('ECT','기타'))
    user=models.ForeignKey(Users, on_delete=models.CASCADE)
    expense=models.IntegerField(blank=False, null=False)
    memo=models.TextField(blank=True, null=True)
    category=models.CharField(max_length=10,choices=cateory_choices)
    date=models.DateField(auto_now_add=True)