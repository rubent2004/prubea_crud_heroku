from django.urls import path, include
from .views import CursoList, CursoCreate, CursoUpdate, CursoDelete
from .views import EstudianteList, EstudianteCreate, EstudianteUpdate, EstudianteDelete
from .views import TareaList, TareaCreate, TareaUpdate, dashboard, TareaDelete
urlpatterns = [

    # Cursos

    path('cursos/', CursoList.as_view(), name='curso_list'),
    path('cursos/nuevo/', CursoCreate.as_view(), name='curso_create'),
    path('cursos/editar/<int:pk>/', CursoUpdate.as_view(), name='curso_edit'),
    path('cursos/eliminar/<int:pk>/', CursoDelete.as_view(), name='curso_delete'),

    # Estudiantes
    path('estudiantes/', EstudianteList.as_view(), name='estudiante_list'),
    path('estudiantes/nuevo/', EstudianteCreate.as_view(), name='estudiante_create'),
    path('estudiantes/editar/<int:pk>/', EstudianteUpdate.as_view(), name='estudiante_edit'),
    path('estudiantes/eliminar/<int:pk>/', EstudianteDelete.as_view(), name='estudiante_delete'),

    # Tareas
    path('tareas/', TareaList.as_view(), name='tarea_list'),
    path('tareas/nueva/', TareaCreate.as_view(), name='tarea_create'),
    path('tareas/editar/<int:pk>/', TareaUpdate.as_view(), name='tarea_edit'),
    path('tareas/eliminar/<int:pk>/', TareaDelete.as_view(), name='tarea_delete'),
]