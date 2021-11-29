from django.db import models

# Create your models here.
class paciente(models.Model):

    Nombre = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
    
    def __str__(self):
        return self.Nombre
    
    # def get_absolute_url(self):
    #     return reverse("Paciente_detail", kwargs={"pk": self.pk})

class tessiu(models.Model): #Herencia

    Temperatura = models.FloatField(verbose_name="Temperatura")
    Color = models.FloatField()
    Inflamation = models.FloatField(verbose_name="Inflamacion")
    #el blank y el null son espacios donde pueden ir nulos
    Nombre = models.ForeignKey(paciente, on_delete=models.CASCADE,blank=True, null=True)

    class Meta:
        verbose_name = "tejido"
        verbose_name_plural = "Tejidos"

    def __str__(self):
        # es la forma en la que se va a imprimir 
        return 'Temperatura '+str(self.Temperatura)+' Color '+str(self.Color) 


    # def get_absolute_url(self): no tiene uso 
    #     return reverse("tablaValores_detail", kwargs={"pk": self.pk})


    