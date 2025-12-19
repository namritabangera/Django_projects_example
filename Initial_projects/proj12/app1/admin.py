from django.contrib import admin
from app1.models import StudentModel

# Register your models here.
class StudentModelAdmin(admin.ModelAdmin):
    list_display=['rollno','course','fees']
    list_display_links=['rollno']
    list_editable=['course','fees']

admin.site.register(StudentModel,StudentModelAdmin)