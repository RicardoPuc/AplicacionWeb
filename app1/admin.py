from django.contrib import admin
from .models import Persona, Curso, Leccion, Pregunta

# Register your models here.
class CursoAdmin(admin.ModelAdmin):
    list_display=("id","nombre",)

class LeccionAdmin(admin.ModelAdmin):
    list_display=("id","nombre",)
    list_filter=("curso",)

class PreguntaAdmin(admin.ModelAdmin):
    list_display=("id","pregunta","respuesta",)





admin.site.register(Persona)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Leccion, LeccionAdmin)
admin.site.register(Pregunta, PreguntaAdmin)

