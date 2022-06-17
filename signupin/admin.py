from django.contrib import admin
from .models import *
# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id','name','review','tick']
admin.site.register(Review, ReviewAdmin)
admin.site.register(MeroTime)

class StudAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'age']
admin.site.register(Stud, StudAdmin)
