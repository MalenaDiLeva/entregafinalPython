from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from Aplicacion.models import Curso
from Aplicacion.models import Profesores
from Aplicacion.models import Alumnos
from Aplicacion.models import Avatar
from django.http import HttpResponse
from django.template import loader
from Aplicacion.forms import Curso_formulario
from Aplicacion.forms import Profesores_formulario
from Aplicacion.forms import Alumnos_formulario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from Aplicacion.forms import Curso_formulario, UserEditForm
from Aplicacion.forms import Profesores_formulario, UserEditForm
from Aplicacion.forms import Alumnos_formulario, UserEditForm
from django.contrib.auth.decorators import login_required
# Create your views here.



def inicio(request):
    
    return render( request , "padre.html")

def ver_cursos(request):
    cursos=Curso.objects.all()
    dicc={"cursos": cursos}
    plantilla=loader.get_template("cursos.html")
    documento=plantilla.render(dicc)

    return render(request, "cursos.html",{ "cursos":cursos})

def alta_curso(request,nombre):
    curso = Curso(nombre=nombre , camada=234512)
    curso.save()
    return render(request, "cursos.html", {"cursos": curso})


 


def ver_alumnos(request):
    alumnos=Alumnos.objects.all()
    dicc={"alumnos": alumnos}
    plantilla=loader.get_template("alumnos.html")
    documento=plantilla.render(dicc)
    return HttpResponse (documento)


def editar_curso(request, id):
    curso=Curso.objects.get(id=id)
    if request.method=="POST":
        pass

    else:
        mi_formulario=Curso_formulario(initial={"nombre":curso.nombre, "camada":curso.camada})
        return render (request, "editar_curso.html", {"mi_formulario": mi_formulario, "curso":curso})


def ver_profesores(request):
    profesores=Profesores.objects.all()
    dicc={"profesores": profesores}
    plantilla=loader.get_template("profesores.html")
    documento=plantilla.render(dicc)
    return HttpResponse(documento)


def curso_formulario(request):
    if request.method=="POST":
        mi_formulario=Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data

            curso=Curso(nombre=datos["nombre"], camada=datos["camada"])
            curso.save()
            curso=Curso.objects.all()
            return render (request, "cursos.html", {"cursos":curso})
        
           

    return render (request, "formulario.html")



def formulario_profesores(request):
    if request.method=="POST":
        formulario=Profesores_formulario(request.POST)
        if formulario.is_valid():
            referencias=formulario.cleaned_data

            profesores=Profesores(nombre=referencias["nombre"], apellido=referencias["apellido"], materia=referencias["materia"])
            profesores.save()
            profesor=Profesores.objects.all()
            return render(request, "profesores.html", {"profesores": profesor})

    return render (request, "altaprofesores.html")

def alumnos_formulario(request):
    if request.method=="POST":
        form=Alumnos_formulario(request.POST)
        if form.is_valid():
            data=form.cleaned_data

            alumnos=Alumnos(nombre=data["nombre"], apellido=data["apellido"])
            alumnos.save()
            alumno=Alumnos.objects.all()
            return render(request, "alumnos.html", {"alumnos": alumno})


    return render (request, "altaalumnos.html")




def buscar_curso(request):

    return render(request, "buscar_curso.html")

def buscar(request):
    if request.GET["nombre"]:
            nombre=request.GET["nombre"]
            cursos = Curso.objects.filter(nombre__icontains= nombre)
            return render (request, "resultado_busqueda.html", {"cursos": cursos})

    else:
        return HttpResponse ("Ingrese en nombre del curso")
    

def buscar_alumnos(request):

    return render(request, "buscar_alumnos.html")

def buscar_a(request):
    if request.GET["apellido"]:
            apellido=request.GET["apellido"]
            alumnos = Alumnos.objects.filter(apellido__icontains= apellido)
            return render (request, "busqueda_a.html", {"alumnos": alumnos})

    else:
        return HttpResponse ("Ingrese el nombre del alumno")
    
def buscar_profesores(request):
    return render(request, "buscar_profesores.html")

def buscar_p(request):
    if request.GET["apellido"]:
            apellido=request.GET["apellido"]
            profesores = Profesores.objects.filter(apellido__icontains= apellido)
            return render (request, "busqueda_p.html", {"profesores": profesores})

    else:
        return HttpResponse ("Ingrese el nombre del profesor")
  
def eliminar_curso(request, id):
    curso=Curso.objects.get(id=id)
    curso.delete()
    curso=Curso.objects.all()
    return render(request, "cursos.html", {"cursos": curso})


def editar(request, id):
    curso=Curso.objects.get(id=id)
    if request.method=="POST":
        mi_formulario=Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            datos=mi_formulario.cleaned_data
            curso.nombre=datos["nombre"]
            curso.camada=datos["camada"]
            curso.save()
            curso=Curso.objects.all()
            return render (request, "cursos.html", {"cursos":curso})

    else:
        mi_formulario=Curso_formulario(initial={"nombre": curso.nombre, "camada":curso.camada})
        return render(request, "editar_curso.html", {"mi_formulario": mi_formulario, "curso":curso})
    

    
def eliminar_profesores(request, id):
    profesores=Profesores.objects.get(id=id)
    profesores.delete()
    profesores=Profesores.objects.all()
    return render(request, "profesores.html", {"profesores": profesores})


def editar_profesor(request, id):
    profesor=Profesores.objects.get(id=id)
    if request.method=="POST":
        formulario=Profesores_formulario(request.POST)
        if formulario.is_valid():
            info=formulario.cleaned_data
            profesor.nombre=info["nombre"]
            profesor.apellido=info["apellido"]
            profesor.materia=info["materia"]
            profesor.save()
            profesor=Profesores.objects.all()
            return render(request, "profesores.html", {"profesores": profesor})



    else:
        formulario=Profesores_formulario(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "materia":profesor.materia})
        return render(request, "editar_profesor.html", {"formulario":formulario, "profesor":profesor})







def eliminar_alumnos(request, id):
    alumnos=Alumnos.objects.get(id=id)
    alumnos.delete()
    alumnos=Alumnos.objects.all()
    return render(request, "alumnos.html", {"alumnos": alumnos})



    
def editar_alumno(request, id):
    alumno=Alumnos.objects.get(id=id)
    if request.method=="POST":
        form=Alumnos_formulario(request.POST)
        if form.is_valid():
            datos_a=form.cleaned_data
            alumno.nombre=datos_a["nombre"]
            alumno.apellido=datos_a["apellido"]
            alumno.save()
            alumno=Alumnos.objects.all()
            return render(request, "alumnos.html", {"alumnos": alumno})


    else:
        form=Alumnos_formulario(initial={"nombre":alumno.nombre, "apellido":alumno.apellido})
        return render(request, "editar_alumno.html", {"form": form, "alumno":alumno})


def login_request(request):
    if request.method =="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            user=authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                avatares=Avatar.objects.filter(user=request.user.id)
                return render(request, "inicio.html", {'url':avatares[0].imagen.url, "mensaje": f"Bienvenido/a {usuario},", "usuario": usuario})
            else:
                return HttpResponse(f"Usuario no encontrado")
        
        else:
            return HttpResponse(f"FORM INCONRRECTO {form}")

    form=AuthenticationForm()

    return render(request, "login.html", {"form" : form})

def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Usuario creado")
        
    else:
        form=UserCreationForm()
        return render(request, "registro.html", {"form": form})

def editar_perfil(request):
    usuario=request.user
    if request.method=="POST":
        mi_formulario=UserEditForm(request.POST)
        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            usuario.email=informacion["email"]
            password=informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            return render(request,'inicio.html')


    else:
        miFormulario=UserEditForm(initial={'email':usuario.email})
        return render (request, "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})

