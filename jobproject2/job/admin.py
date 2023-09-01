from django.contrib import admin
from job.models import Development,Hacking,DebugTester
# Register your models here.
class DevelopmentAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(Development,DevelopmentAdmin)

class HackingAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(Hacking,HackingAdmin)

class DebugTesterAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(DebugTester,DebugTesterAdmin)
