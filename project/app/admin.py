from django.contrib import admin

# Register your models here.
# Register your models here
from .models import User,Educational_info,Professional_info,Desired_person,Family_info,Iitial_info,Contact_info,Prposals,Image

admin.site.register(User)
admin.site.register(Iitial_info)
admin.site.register(Family_info)
admin.site.register(Educational_info)
admin.site.register(Professional_info)
admin.site.register(Desired_person)
admin.site.register(Contact_info)
admin.site.register(Prposals)
admin.site.register(Image)
