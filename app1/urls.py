from django.urls import path
from .views import CreatePersona, ListPersona, UpdatePersona, DeletePersona, CreateCurso, ListCurso, UpdateCurso, DeleteCurso, CreateLeccion, UpdateLeccion, ListLeccion, DeleteLeccion, CreatePregunta, UpdatePregunta, ListPregunta, DeletePregunta, ListEstudiante, ListTomarleccion




urlpatterns=[
    
    path(r'crear_persona/', CreatePersona.as_view(), name='crear_persona'),
    path(r'listar_persona/', ListPersona.as_view(), name='listar_persona'),
    path(r'editar_persona/(?P<pk>\d+)/$', UpdatePersona.as_view(), name='editar_persona'),
    path(r'eliminar_persona/(?P<pk>\d+)/$', DeletePersona.as_view(), name='eliminar_persona'),

    path(r'crear_curso/', CreateCurso.as_view(), name='crear_curso'),
    path(r'listar_curso/', ListCurso.as_view(), name='listar_curso'),
    path(r'editar_curso/(?P<pk>\d+)/$', UpdateCurso.as_view(), name='editar_curso'),
    path(r'eliminar_curso/(?P<pk>\d+)/$', DeleteCurso.as_view(), name='eliminar_curso'),

     path(r'inicio/', ListEstudiante.as_view(), name='inicio'),

    path(r'crear_leccion/', CreateLeccion.as_view(), name='crear_leccion'),
    path(r'listar_leccion/', ListLeccion.as_view(), name='listar_leccion'),
    path(r'editar_leccion/(?P<pk>\d+)/$', UpdateLeccion.as_view(), name='editar_leccion'),
    path(r'eliminar_leccion/(?P<pk>\d+)/$', DeleteLeccion.as_view(), name='eliminar_leccion'),

      path(r'tomar_leccion/', ListTomarleccion.as_view(), name='tomar_leccion'),

    path(r'crear_pregunta/', CreatePregunta.as_view(), name='crear_pregunta'),
    path(r'listar_pregunta/', ListPregunta.as_view(), name='listar_pregunta'),
    path(r'editar_pregunta/(?P<pk>\d+)/$', UpdatePregunta.as_view(), name='editar_pregunta'),
    path(r'eliminar_pregunta/(?P<pk>\d+)/$', DeletePregunta.as_view(), name='eliminar_pregunta'),
]