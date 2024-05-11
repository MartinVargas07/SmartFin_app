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

class Categoría(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=10) # "ingreso" o "egreso"

class Presupuesto(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoría = models.ForeignKey(Categoría, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

class Objetivo(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoría = models.ForeignKey(Categoría, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_límite = models.DateField()

class AnálisisTendencia(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoría = models.ForeignKey(Categoría, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    monto_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    monto_final = models.DecimalField(max_digits=10, decimal_places=2)

class IntegraciónCuentaBancaria(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    número_cuenta = models.CharField(max_length=20)
    banco = models.CharField(max_length=50)

class ReconocimientoPatrón(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoría = models.ForeignKey(Categoría, on_delete=models.CASCADE)
    patrón = models.CharField(max_length=50) # Ejemplo: "gasto mensual en servicios públicos"

class AlertaNotificación(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoría = models.ForeignKey(Categoría, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50) # Ejemplo: "gasto excedido"
    mensaje = models.CharField(max_length=100)


class SoporteMultiMoneda(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    moneda = models.CharField(max_length=10) # Ejemplo: "USD"
    tasa_cambio = models.DecimalField(max_digits=10, decimal_places=2)


class HerramientaInversiónAhorro(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    descripción = models.CharField(max_length=100)
    monto_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    monto_actual = models.DecimalField(max_digits=10, decimal_places=2)


class CompartirColaborar(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    correo_colaborador = models.EmailField()
    categoría = models.ForeignKey(Categoría, on_delete=models.CASCADE)


class AnálisisRiesgo(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoría = models.ForeignKey(Categoría, on_delete=models.CASCADE)
    nivel_riesgo = models.CharField(max_length=50) # Ejemplo: "alto", "medio", "bajo"
