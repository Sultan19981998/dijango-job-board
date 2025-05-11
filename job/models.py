from django.db import models
from django.template.defaultfilters import title

Jop_Type=(('Full Type','Full Type'),
          ('Part Type','Part Type'),)





class Job(models.Model):
    title=models.CharField(max_length=100)
    job_type=models.CharField(max_length=15,choices=Jop_Type)
    decreption=models.TextField(max_length=1000)
    date_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)


    def __str__(self):
        return self.title
