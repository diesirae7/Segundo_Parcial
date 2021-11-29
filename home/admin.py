from django.contrib import admin
from .models import tessiu, paciente
# Register your models here.

class tessiuAdmin(admin.ModelAdmin):
    list_display = ('Temperatura','Color','Inflamation')
    search_fields = ('Temperatura',) #<----> Busquedas

admin.site.register(tessiu, tessiuAdmin)

class pacienteAdmin(admin.ModelAdmin):
    list_display = ('Nombre',)

admin.site.register(paciente, pacienteAdmin)


