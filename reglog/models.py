from django.db import models

# Create your models here.


class registration(models.Model):
    email = models.EmailField(max_length=100,primary_key=True) 
    name = models.CharField(max_length=100,default="")
    password = models.CharField(max_length=50,default="")
    phone = models.IntegerField(unique=True,default="")
    con_password = models.CharField(max_length=50,default="")
    
class all_details(models.Model):
    roll_number = models.CharField(max_length=100)
    email1 = models.ForeignKey(registration,on_delete=models.CASCADE)    

class student_details_1(models.Model):
    roll_number = models.ForeignKey(all_details, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,default="")
    last_name = models.CharField(max_length=50,default="")
    class_student = models.CharField(max_length=50,default="")
    maths = models.IntegerField(default="")
    hindi = models.IntegerField(default="")
    english = models.IntegerField(default="")
    enviromental_science = models.IntegerField(default="")
    # email1 = models.ForeignKey("registration", on_delete= models.CASCADE)


class student_details_2(models.Model):
    roll_number = models.ForeignKey(all_details, on_delete= models.CASCADE)
    first_name = models.CharField(max_length=100,default="")
    last_name = models.CharField(max_length=50,default="")
    class_student = models.CharField(max_length=50,default="")
    maths = models.IntegerField(default="")
    hindi = models.IntegerField(default="")
    english = models.IntegerField(default="")
    science = models.IntegerField(default="")
    social_studies = models.IntegerField(default="")
    