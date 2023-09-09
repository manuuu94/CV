from django.contrib import admin
from .models import Personal,Languages,Profile,WorkXP,Education,Skills,skillDetails,otherValues,cvTitles,PortfolioImg,PortfolioSkills

# Register your models here.


admin.site.register(Personal)
admin.site.register(Languages)
admin.site.register(Profile)
admin.site.register(WorkXP)
admin.site.register(Education)
admin.site.register(Skills)
admin.site.register(skillDetails)
admin.site.register(otherValues)

admin.site.register(cvTitles)
admin.site.register(PortfolioImg)
admin.site.register(PortfolioSkills)




