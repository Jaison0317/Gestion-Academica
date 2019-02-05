from django.db import models

# Create your models here.

class Alumno(models.Model):

    Primer_Apellido= models.CharField(max_length=40)
    Segundo_Apellido=models.CharField(max_length=40)
    Nombres = models.CharField(max_length=50)
    Cedula = models.CharField(max_length=11)
    FechaDeNacimiento = models.DateTimeField()
    Sexos = (('F', 'Femenino'), ('M', 'Masculino'))
    Sexo=models.CharField(max_length=1, choices=Sexos, default='M')

    def NombreCompleto(self):
        cadena ="{0} {1}, {2}"
        return cadena.format(self.Primer_Apellido, self.Segundo_Apellido, self.Nombres)

    def __str__(self):
        return self.NombreCompleto()


class Curso(models.Model):
    Nombre = models.CharField(max_length=50)
    Creditos = models.PositiveSmallIntegerField()
    Estado = models.BooleanField(default=True)

    def __str__(self):
        return "{0} ({1}), {2}".format(self.Nombre, self.Creditos)


class Matricula(models.Model):
    Alumno = models.ForeignKey(Alumno, null=False, blank=False, on_delete=models.CASCADE)
    Curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    FechaDeMatricula = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        cadena = "{0} => {1}"
        return cadena.format(self.Alumno, self.Curso.Nombre)


class Profesores(models.Model):
    Nombres = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    Asignatura = models.CharField(max_length=35)


    def __str__(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.Nombres, self.Apellidos, self.Asignatura)
