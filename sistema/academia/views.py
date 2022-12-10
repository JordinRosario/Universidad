from django.shortcuts import render




# Create your views here.
def home(request):
    
    return render(request,'home.html')

def casa_estudiante(request):
    return render(request, 'casa_estudiante.html')





