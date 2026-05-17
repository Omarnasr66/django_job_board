from django.db import models

#craete your models here

'''
django modle field :
    _ html widget
    _ validation
    _ db size
'''

JOB_TYPE =(
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time"),
)
class Job(models.Model): #table 
    title = models.CharField(max_length=100) #column
    #location 
    job_type = models.CharField(max_length=15, choices=JOB_TYPE) #full time, part time, internship
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name