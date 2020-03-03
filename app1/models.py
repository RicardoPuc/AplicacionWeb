from django.db import models

# Create your models here.

class Persona(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=200)
    apellido=models.CharField(max_length=255)
    edad=models.IntegerField()
    telefono=models.CharField(max_length=10)

class Curso(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=200)
    profesor=models.CharField(max_length=200)
    descripcion=models.TextField()
    certificacion=models.BooleanField()
    

    def __str__(self):
        return self.nombre

leccion_status =[
    (1,'Disponibles'),
    (0, 'No Disponible'),
]

class Leccion(models.Model):
    id=models.AutoField(primary_key=True)
    curso = models.ForeignKey(Curso, null=True, blank=True, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=200)
    puntos=models.IntegerField()
    status=models.IntegerField(null=True, blank=True, choices=leccion_status)
    

    def __str__(self):
        return self.nombre



class Pregunta(models.Model):
    id=models.AutoField(primary_key=True)
    Leccion=models.ForeignKey(Leccion,null=True, blank=True, on_delete=models.CASCADE)
    pregunta=models.CharField(max_length=255, null=True, blank=True)
    respuesta=models.CharField(max_length=500, null=True, blank=True)
  
