from django.db import models

# Create your models here.
class name(models.Model):
    fname=models.CharField(max_length=16)
    lname=models.CharField(max_length=11)
    username=models.CharField(unique=True,max_length=16)
class regform(models.Model):
    MobileNumber=models.IntegerField(null=False)
    DateOfBirth=models.DateField(null=False)
    Age=models.IntegerField(null=False)
    Gender=models.CharField(max_length=10)
    EmailID=models.EmailField(unique=False,max_length=21)
    KnownLang= models.CharField(max_length=18)
    Country=models.CharField(max_length=20)
    Address=models.CharField(max_length=45)
class per_info(models.Model):
    FatherName= models.CharField(max_length=16)
    MartialStatus= models.CharField(max_length=17)
    Edu_Qua= models.CharField(max_length=12)
    YearOfPassing = models.IntegerField(null=True)
class profo_details(models.Model):
    Cur_Company= models.CharField(max_length=17)
    Reliving_Date= models.DateField(null=False)
    New_Company= models.CharField(max_length=15)
    Experience=  models.IntegerField(null=True)
class post_salary(models.Model):
    Designation= models.CharField(max_length=20)
    salary= models.IntegerField(null=True)
class expec_salary(models.Model):
    Designation= models.CharField(max_length=20)
    expect_salary= models.IntegerField(null=True)
class information(models.Model):
    Full_Name= models.CharField(max_length=20)
    Professional=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    DateOfBirth=models.DateField(null=False)
    MobileNumber=models.IntegerField(null=True)
    EmailID=models.EmailField(unique=False,max_length=21)
    Country=models.CharField(max_length=20)
    State=models.CharField(max_length=30)
    District=models.CharField(max_length=30)
    Location=models.CharField(max_length=20)
class signup(models.Model):
    fname= models.CharField(max_length=16)
    lname= models.CharField(max_length=16)
    DateOfBirth= models.DateField(null=False)
    Age= models.IntegerField(null=True)
    Gender=models.CharField(max_length=20)
    KnownLang= models.CharField(max_length=16)
    EmailId=models.CharField(max_length=16, unique=True)
    EmailId_1= models.CharField(max_length=16)
    pass_1 = models.CharField(max_length=16)
    pass_2= models.CharField(max_length=16)



    
