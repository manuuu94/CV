import datetime
import os
from django.http import HttpResponse
from django.shortcuts import render
from . import models
# Create your views here.


def my_cv(request):
    personalData = models.Personal.objects.get(pk=1)
    name = personalData
    phone = personalData.phone
    email = personalData.email
    birthDate = personalData.birthDate
    address = personalData.address
    img = str(personalData.img)
    imgBasePath = os.path.basename(img)
    value = "option1"
    languages = models.Languages.objects.all()
    profileDesc = models.Profile.objects.all()
    dict = {"data":{
            "Phone":phone,
            "Email":email,
            "Birthdate":birthDate,
            "Address":address,
            "GitHub":personalData.github       
            },
            "fullName":name,
            "img":imgBasePath,
            "languages":languages,
            "button":value,
            "description":profileDesc[0],
            }  
    dict["xpWork"] = workXP() 
    dict["skills"] = Skills()
    dict["Education"] = Education()
    dict["skillDetails"] = skillDetailsfunction()   
    dict["skillImg"] = skillImg()
    dict["Titles"] = Titles()
    dict["buttons"] = buttonTitles()
    if request.method == 'POST':
        value = request.POST.get('button')
    dict["button"] = value
    return render(request,'my_cv/manucv.html',context = dict)

def buttonTitles():
      titles = models.cvTitles.objects.all()
      new_dict = {"Profile":{"btn1":f"{titles[2]}","num":1},
                  "Skills":{"btn1":f"{titles[3]}","num":2},
                  "WorkExperience":{"btn1":f"{titles[4]}","num":3},
                  "Education":{"btn1":f"{titles[5]}","num":4}
                  }
      return new_dict

def Titles():
      titles = models.cvTitles.objects.all()
      new_dict = {"PersonalData":titles[0],
                  "Languages":titles[1],
                  "Profile":titles[2],
                  "Skills":titles[3],
                  "WorkExperience":titles[4],
                  "Education":titles[5],
                  "EducationCertificates":titles[6]}  
      return new_dict

def workXP():
    workXP = models.WorkXP.objects.all()
    indexWork = 0
    new_dict = {}
    for work in workXP:
        year_monthFrom = str(work.fromDate)
        year_monthFrom = year_monthFrom[:7]
        if work.toDate is not None:
                year_monthTo = str(work.toDate)
                year_monthTo = year_monthTo[:7]
                fromTo = (f"From: {year_monthFrom} To: {year_monthTo}")
        else:
                fromTo = (f"From: {year_monthFrom}")

        new_dict[f"work{indexWork}"] = {"description":f"{work}","position":indexWork, "fromTo": fromTo}
        indexWork = indexWork+1
    return new_dict

def Skills():
        skills = models.Skills.objects.all()
        indexSkills = 0
        new_dict = {}
        for skill in skills:   
                new_dict[f"skill{indexSkills}"] = skill
                indexSkills = indexSkills+1    
        return new_dict
        
def Education():
        educations = models.Education.objects.all()
        indexEducation = 0
        new_dict = {}
        for education in educations:  
            if education.img is None:                
                new_dict[indexEducation] ={"academy":education.institution,"description":education.description,"status":education.status,"progress":education.progress,"cert":None}
                indexEducation = indexEducation+1
            else:
                img = str(education.img)
                imgBasePath = os.path.basename(img)
                new_dict[indexEducation] ={"academy":education.institution,"description":education.description,"status":education.status,"progress":education.progress,"cert":imgBasePath}
                indexEducation = indexEducation+1
        return new_dict

def skillDetailsfunction():
        skillDetails = models.skillDetails.objects.all()
        indexSkill = 0
        new_dict = {}
        for skill in skillDetails:               
            new_dict[indexSkill] ={"skill":f"{skill}","yrs":skill.yearsPractice}
            indexSkill = indexSkill+1
        return new_dict

def skillImg():
        skillDetails = models.skillDetails.objects.all()
        indexSkillImg = 0
        new_dict = {}
        for skill in skillDetails:  
                skillimg = str(skill.img)
                skillimgBasePath = os.path.basename(skillimg)            
                new_dict[indexSkillImg] = {"img":skillimgBasePath}
                indexSkillImg = indexSkillImg+1
        return new_dict