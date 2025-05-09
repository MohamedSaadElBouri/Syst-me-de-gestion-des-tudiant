from django.contrib import admin
from .models import Student, GuidEtudiant, CalendarEvent, Formulaire
from django.contrib import admin

class StudentAdmin(admin.ModelAdmin):
    fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'gpa', 'img', 'age', 'baccalaureat_mark', 'absences']
    list_display = ('student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'gpa')

class GuidEtudiantAdmin(admin.ModelAdmin):
    list_display = ['title', 'pdf_file']

class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_date']

class FormulaireAdmin(admin.ModelAdmin):
    list_display = ['name', 'form_file']
admin.site.register(Student, StudentAdmin)
admin.site.register(GuidEtudiant, GuidEtudiantAdmin)
admin.site.register(CalendarEvent, CalendarEventAdmin)
admin.site.register(Formulaire, FormulaireAdmin)

