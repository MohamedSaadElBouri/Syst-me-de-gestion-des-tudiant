from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student, GuidEtudiant, CalendarEvent, Formulaire
from .forms import StudentForm, ConnexionForm, UserRegistrationForm

def index(request):
    students = Student.objects.all()
    guides = GuidEtudiant.objects.all()
    events = CalendarEvent.objects.all()
    forms = Formulaire.objects.all()
    
    return render(request, 'students/index.html', {
        'students': students,
        'guides': guides,
        'events': events,
        'forms': forms,
        'show_download': True
    })


def view_student(request, id):
    
    student = Student.objects.get(id=id)
    return render(request, 'students/view_student.html', {'student': student})

def add_student(request):
    
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})

def view_guid(request, id):
    # Logique pour afficher un guide
    return render(request, 'students/view_guid.html')

def calendar(request):
    # Logique pour afficher le calendrier
    return render(request, 'students/calendar.html')

def view_formulaire(request, id):
    # Logique pour afficher un formulaire
    return render(request, 'students/view_formulaire.html')



def download_page(request):
    guides = GuidEtudiant.objects.all()
    events = CalendarEvent.objects.all()
    forms = Formulaire.objects.all()
    
    return render(request, 'students/index.html', {
        'guides': guides,
        'events': events,
        'forms': forms,
        'show_download': True
    })

def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if username == 'saad' and password == 'saad.er2006':
                    return render(request, 'choix_page.html')
                else:
                    login(request, user)
                    next_url = request.GET.get('next', 'index')
                    return redirect(next_url)
            
    else:
        form = ConnexionForm()
    return render(request, 'students/connexion.html', {'form': form})

def inscription(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Création automatique du profil utilisateur si nécessaire
            try:
                from .models import UserProfile
                UserProfile.objects.create(user=user)
            except:
                pass
            
            # Connexion automatique après inscription
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'students/inscription.html', {'form': form})

def deconnexion(request):
    logout(request)
    return redirect('index')
