from django.db import models

# 1. Modelo Profesor
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

# 2. Modelo Curso (Relación Muchos a Uno con Profesor)
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    # ForeignKey: Un curso tiene un profesor, un profesor tiene muchos cursos.
    # on_delete=models.CASCADE: Si borran al profesor, se borran sus cursos.
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='cursos')

    def __str__(self):
        return self.nombre

# 3. Modelo Estudiante
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Relación Muchos a Muchos con Curso a través de la tabla intermedia 'Inscripcion'
    cursos = models.ManyToManyField(Curso, through='Inscripcion', related_name='estudiantes')

    def __str__(self):
        return self.nombre

# 4. Modelo Perfil (Relación Uno a Uno con Estudiante)
class Perfil(models.Model):
    # OneToOneField: Un estudiante tiene un solo perfil único.
    estudiante = models.OneToOneField(Estudiante, on_delete=models.CASCADE)
    biografia = models.TextField(blank=True)
    foto = models.CharField(max_length=200, blank=True)
    redes = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Perfil de {self.estudiante.nombre}"

# 5. Modelo Intermedio Inscripcion
class Inscripcion(models.Model):
    ESTADOS = [
        ('ACT', 'Activo'),
        ('FIN', 'Finalizado'),
    ]

    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    
    # Campos adicionales solicitados
    fecha_inscripcion = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=3, choices=ESTADOS, default='ACT')
    nota_final = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    class Meta:
        # Asegura que un estudiante no se inscriba dos veces al mismo curso
        unique_together = ('estudiante', 'curso')

    def __str__(self):
        return f"{self.estudiante} en {self.curso} ({self.get_estado_display()})"