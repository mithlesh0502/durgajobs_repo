from django.contrib import admin
from testApp.models import hydjobs,bangalorejobs,chennaijobs,punejobs

# Register your models here.
class hydjobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']

class bangalorejobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']

class chennaijobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']

class punejobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibility','address','email','phonenumber']

admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(bangalorejobs,bangalorejobsAdmin)
admin.site.register(chennaijobs,chennaijobsAdmin)
admin.site.register(punejobs,punejobsAdmin)