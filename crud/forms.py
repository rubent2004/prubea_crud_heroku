from django import forms
from .models import Curso, Estudiante, Tarea

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'codigo']

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'matricula']

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_entrega', 'tipo_tarea', 'curso']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3, 'cols': 50}),  # Ajusta las filas y columnas según tus necesidades
            'fecha_entrega': forms.DateInput(attrs={'type': 'date'}),
        }