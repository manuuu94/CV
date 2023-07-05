from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
  

class Personal(models.Model):
    name = models.CharField(max_length=60)
    middleName = models.CharField(max_length=60)
    lastName1 = models.CharField(max_length=60)
    lastName2 = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    birthDate = models.DateField()
    img = models.ImageField(upload_to='my_cv/static/my_cv/img')
    address = models.CharField(max_length=600)
    github = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.middleName} {self.lastName1} {self.lastName2}"


class Languages(models.Model):
    language = models.CharField(max_length=60)
    level = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.language} - {self.level}"




class Profile(models.Model):
    description = models.CharField(max_length=1500)

    def __str__(self):
        return self.description


class Skills(models.Model):
    skillName = models.CharField(max_length=500)
    yearsPractice = models.DecimalField(decimal_places=1,max_digits=3,null=True,blank=True)

    def __str__(self):
        return f"{self.skillName}"


class skillDetails(models.Model):
    skillName = models.CharField(max_length=500)
    yearsPractice = models.DecimalField(decimal_places=2,max_digits=3,null=True,blank=True)
    img = models.ImageField(upload_to='my_cv/static/my_cv/img/skills')

    def __str__(self):
        return f"{self.skillName}"  
    

class WorkXP(models.Model):
    companyName = models.CharField(max_length=100)
    fromDate = models.DateField()
    toDate = models.DateField(blank=True, null=True)
    position = models.CharField(max_length=100)
    jobDescription = models.CharField(max_length=1000)

    def __str__(self):
        if self.toDate is None:
            return  f"{self.position} - {self.companyName} (from: {self.fromDate}): {self.jobDescription}"
        else: 
            return f"{self.position} - {self.companyName} (from: {self.fromDate} to: {self.toDate}): {self.jobDescription}"


class Education(models.Model):
    institution = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    status = models.CharField(max_length=100)
    progress = models.IntegerField()
    img = models.ImageField(upload_to='my_cv/static/my_cv/img/certs',null=True,blank=True)


    def __str__(self):
        return f"{self.institution}: {self.description} ({self.status})"



class otherValues(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='my_cv/static/my_cv/img/profile')



class cvTitles(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"





















