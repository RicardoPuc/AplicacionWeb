from django import forms
from .models import Persona, Curso, Leccion, Pregunta


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields=[
            'nombre',
            'apellido',
            'edad',
            'telefono',
        
        ]

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields=[
            'nombre',
            'profesor',
            'descripcion',
            'certificacion',
        ]
class EstudianteForm(forms.ModelForm):
    class Meta:
        model =Curso
        fields=[
            'nombre',
            'profesor',
            'descripcion',
            'certificacion',
        ]

class LeccionForm(forms.ModelForm):
    class Meta:
        model = Leccion
        fields=[
            'curso',
            'nombre',
            'puntos',
            'status',
    
        ]
class TomarleccionForm(forms.ModelForm):
    class Meta:
        model = Leccion
        fields=[
            'curso',
            'nombre',
            'puntos',
            'status',
    
        ]
class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields=[
            'Leccion',
            'pregunta',
            'respuesta',
            
           
        ]