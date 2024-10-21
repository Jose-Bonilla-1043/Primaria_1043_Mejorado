from django.shortcuts import render
from .models import Alumno
# Create your views here.

def index_vista(request):
    MisAlumnos = Alumno.objects.all().order_by("id")
    return render(request, "index.html", {"MisAlumnos":MisAlumnos})