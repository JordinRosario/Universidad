from django.db import models

# Create your models here.
class Carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=35)
    duracion = models.PositiveSmallIntegerField(default=5)
    
    def __str__(self) -> str:
        return f'{self.nombre} codigo {self.codigo} duracion {self.duracion} años'
    
class Estudiante(models.Model):
    dni = models.CharField(max_length=10, primary_key=True)
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    nombre = models.CharField(max_length=35, null = False, blank = False)
    fecha_nacimineto = models.DateField(null = False, blank=False)
    sexos = [
        ('M','Masculino'),
        ('F','Femenino')
        ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F' )
    carrera= models.ForeignKey(Carrera, null =False , blank= False, on_delete = models.CASCADE) # On delete si un estudiante depende de una carrera y se borra la carrera todos los estudiantes que pertenecen a esa carrera seran eliminados
    vigencia = models.BooleanField()
    
    def nombre_completo(self):
        return f'{self.apellidoPaterno} { self.apellidoMaterno} {self.nombre}'
    
    
    """ Vizualiza los nombres en los registros de estudiantes """
    def __str__(self):
        if self.vigencia: 
            estado_estudiante = 'ACTIVO'
        else: 
            estado_estudiante = 'DE BAJA'
            
        return f'{self.nombre_completo()} carrera:{self.carrera} estado: {estado_estudiante} '


class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f'{self.nombre} docente: {self.docente}, creditos {self.creditos}'
    
    
class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, null = False, blank = False, on_delete=models.CASCADE)
    nombre = models.ForeignKey(Curso, null=False, blank = False, on_delete = models.CASCADE)
    fecha_matricula = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        
        return f'estudiante {self.estudiante.nombre_completo()} curso {self.nombre} se registro {self.fecha_matricula}'
