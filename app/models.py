from django.db import models

# Create your models here.
class School(models.Model):
    School_Name=models.CharField(max_length=50)


    def __str__(self):
        return self.School_Name



class Student(models.Model):
    School_Name=models.ForeignKey(School,on_delete=models.CASCADE)
    Student_Name=models.CharField(max_length=20)
    Student_ID=models.IntegerField()
    Student_Address=models.CharField(max_length=40)


    def __str__(self):
        return self.Student_Name
    




