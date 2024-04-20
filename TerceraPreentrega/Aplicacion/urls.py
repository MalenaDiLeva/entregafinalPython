from django.urls import path
from.import views

from django.urls import path
from.import views

from django.contrib.auth.views import LogoutView

urlpatterns=[
    path("alta_curso/<nombre>", views.alta_curso),
    path("alta_curso", views.curso_formulario),
    path("", views.inicio, name="home"),
    path("ver_cursos", views.ver_cursos, name="cursos"),
    path("ver_alumnos", views.ver_alumnos, name= "alumnos"),
    path("ver_profesores", views.ver_profesores, name="profesores"),
    path("alta_profesores", views.formulario_profesores),
    path("alta_alumnos", views.alumnos_formulario),
    path("buscar_curso", views.buscar_curso),
    path("buscar", views.buscar),
    path("buscar_alumnos", views.buscar_alumnos),
    path("buscar_a", views.buscar_a),
    path("buscar_profesores", views.buscar_profesores),
    path("buscar_p", views.buscar_p),
    path("eliminar_curso/<int:id>", views.eliminar_curso, name="eliminar_curso"),
    path("editar_curso/<int:id>", views.editar, name="editar_curso"),
    path("eliminar_profesores/<int:id>", views.eliminar_profesores, name="eliminar_prof"),
    path("editar_profesor/<int:id>", views.editar_profesor, name="editar_profe"),
    path("eliminar_alumnos/<int:id>", views.eliminar_alumnos, name="eliminar_alum"),
    path("editar_alumno/<int:id>", views.editar_alumno, name="editar_alum"),
    path("login", views.login_request, name="login"),
    path("register", views.register, name="register"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path("editar_perfil", views.editar_perfil, name="editarPerfil")
]