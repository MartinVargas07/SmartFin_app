from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=50)

class Transacción(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoría = models.ForeignKey(Categoría, on_delete=models.CASCADE)
    fecha = models.DateField()
    descripción = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=10) # "ingreso" o "egreso"
