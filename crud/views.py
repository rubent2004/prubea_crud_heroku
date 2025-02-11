from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Curso, Estudiante, Tarea
from .forms import CursoForm, EstudianteForm, TareaForm


def dashboard(request):
    # Obtener estadísticas básicas
    total_cursos = Curso.objects.count()
    total_estudiantes = Estudiante.objects.count()
    total_tareas = Tarea.objects.count()

    # Obtener las últimas tareas pendientes (puedes ajustar el número)
    tareas_pendientes = Tarea.objects.order_by('fecha_entrega')[:5]

    context = {
        'total_cursos': total_cursos,
        'total_estudiantes': total_estudiantes,
        'total_tareas': total_tareas,
        'tareas_pendientes': tareas_pendientes,
    }
    return render(request, 'dashboard.html', context)
# Vistas para Cursos
class CursoList(ListView):
    model = Curso
    template_name = 'curso/curso_list.html'

class CursoCreate(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'curso/curso_form.html'
    success_url = reverse_lazy('curso_list')

class CursoUpdate(UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'curso/curso_form.html'
    success_url = reverse_lazy('curso_list')

class CursoDelete(DeleteView):
    model = Curso
    template_name = 'curso/curso_confirm_delete.html'
    success_url = reverse_lazy('curso_list')

# Vistas para Estudiantes (misma estructura que cursos)
class EstudianteList(ListView):
    model = Estudiante
    template_name = 'estudiante/estudiante_list.html'

class EstudianteCreate(CreateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'estudiante/estudiante_form.html'
    success_url = reverse_lazy('estudiante_list')

class EstudianteUpdate(UpdateView):
    model = Estudiante
    form_class = EstudianteForm
    template_name = 'estudiante/estudiante_form.html'
    success_url = reverse_lazy('estudiante_list')

class EstudianteDelete(DeleteView):
    model = Estudiante
    template_name = 'estudiante/estudiante_confirm_delete.html'
    success_url = reverse_lazy('estudiante_list')

# Vistas para Tareas
class TareaList(ListView):
    model = Tarea
    template_name = 'tarea/tarea_list.html'

class TareaCreate(CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tarea/tarea_form.html'
    success_url = reverse_lazy('tarea_list')

class TareaUpdate(UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tarea/tarea_form.html'
    success_url = reverse_lazy('tarea_list')

class TareaDelete(DeleteView):
    model = Tarea
    template_name = 'tarea/tarea_confirm_delete.html'
    success_url = reverse_lazy('tarea_list')