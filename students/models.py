from django.db import models
from django.contrib.auth.models import User  # Utilisation du modèle User par défaut de Django

# N'utilisez plus de modèle User personnalisé

class Student(models.Model):
    student_number = models.PositiveIntegerField()
    img = models.ImageField(upload_to='student_images/', null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=50)
    gpa = models.FloatField()
    age = models.PositiveIntegerField(null=True, blank=True)
    baccalaureat_mark = models.FloatField(null=True, blank=True)
    absences = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'


class GuidEtudiant(models.Model):
    title = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='guid_etudiant_pdfs/')
    
    def __str__(self):
        return self.title

class CalendarEvent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    event_date = models.DateTimeField()
    
    def __str__(self):
        return f'{self.title} - {self.event_date}'

class Formulaire(models.Model):
    name = models.CharField(max_length=100)
    form_file = models.FileField(upload_to='formulaires/')
    
    def __str__(self):
        return self.name


    
    def __str__(self):
        return self.titre