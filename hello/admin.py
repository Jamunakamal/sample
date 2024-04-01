from django.contrib import admin
from .models import name,information,regform,per_info,profo_details,post_salary,expec_salary,signup

# Register your models here.
admin.site.register(name)
admin.site.register(regform)
admin.site.register(per_info)
admin.site.register(profo_details)
admin.site.register(post_salary)
admin.site.register(expec_salary)
admin.site.register(information)
admin.site.register(signup)

