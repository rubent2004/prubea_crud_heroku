
from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    matricula = models.CharField(max_length=15, unique=True)
    cursos = models.ManyToManyField(Curso, through='Inscripcion')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Tarea(models.Model):
    TIPO_TAREA_CHOICES = [
        ('Parcial', 'Parcial'),
        ('Laboratorio', 'Laboratorio'),
        ('Examen', 'Examen'),
        ('Otro', 'Otro'),
    ]
    titulo = models.CharField(max_length=110)
    descripcion = models.TextField()
    fecha_entrega = models.DateField()
    tipo_tarea = models.CharField(max_length=20, choices=TIPO_TAREA_CHOICES)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('estudiante', 'curso')

    def __str__(self):
        return f"{self.estudiante} inscrito en {self.curso}"

class table(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name