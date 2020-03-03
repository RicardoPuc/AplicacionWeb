from django.shortcuts import render, redirect
from .models import Persona, Curso, Leccion, Pregunta
from .forms import PersonaForm, CursoForm, LeccionForm, PreguntaForm, EstudianteForm
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

def inicio(request):
    titulo = "HOLA"


    context = {
        "titulo": titulo,

    }

  

    return render(request,"inicio.html",context)


class CreatePersona(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('listar_persona')

class ListPersona(ListView):
    model = Persona
    template_name = 'listar_persona.html'

class UpdatePersona(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('listar_persona')

class DeletePersona(DeleteView):
    model = Persona
    template_name = 'eliminar_persona.html'
    success_url = reverse_lazy('listar_persona')

#CRUD Cursos

class CreateCurso(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'crear_curso.html'
    success_url = reverse_lazy('listar_curso')

class ListCurso(ListView):
    model = Curso
    template_name = 'listar_curso.html'

class UpdateCurso(UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'crear_curso.html'
    success_url = reverse_lazy('listar_curso')

class DeleteCurso(DeleteView):
    model = Curso
    template_name = 'eliminar_curso.html'
    success_url = reverse_lazy('listar_curso')

class ListEstudiante(ListView):
    model = Curso
    form_class = EstudianteForm
    template_name = 'inicio.html'

#CRUD Lecciones

class CreateLeccion(CreateView):
    model = Leccion
    form_class = LeccionForm
    template_name = 'crear_leccion.html'
    success_url = reverse_lazy('listar_leccion')

class ListLeccion(ListView):
    model = Leccion
    template_name = 'listar_leccion.html'

class UpdateLeccion(UpdateView):
    model = Leccion
    form_class = LeccionForm
    template_name = 'crear_leccion.html'
    success_url = reverse_lazy('listar_leccion')

class DeleteLeccion(DeleteView):
    model = Leccion
    template_name = 'eliminar_leccion.html'
    success_url = reverse_lazy('listar_leccion')

class ListTomarleccion(ListView):
    model = Leccion
    template_name = 'tomar_leccion.html'
    
#CRUD PREGUNTAS

class CreatePregunta(CreateView):
    model = Pregunta
    form_class = PreguntaForm
    template_name = 'crear_pregunta.html'
    success_url = reverse_lazy('listar_pregunta')

class ListPregunta(ListView):
    model = Pregunta
    template_name = 'listar_pregunta.html'

class UpdatePregunta(UpdateView):
    model = Pregunta
    form_class = PreguntaForm
    template_name = 'crear_pregunta.html'
    success_url = reverse_lazy('listar_pregunta')

class DeletePregunta(DeleteView):
    model = Pregunta
    template_name = 'eliminar_pregunta.html'
    success_url = reverse_lazy('listar_pregunta')