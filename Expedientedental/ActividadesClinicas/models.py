from django.db import models 
from altas.models import Medico,Paciente
from datetime import date

#from django.contrib import models

# Create your models here.

class Interrogatorio(models.Model):
	paciente	= models.ForeignKey(Paciente)
	medico	= models.ForeignKey(Medico)
	ultimaVisitaMedica = models.DateField(blank=True, null=True)
	medicamentoUltimosDosAnios = models.CharField(max_length=100, null=False)
	alergicoaMedicamentos = models.CharField(max_length=100, null=False)
	alergicoaanestesicos = models.CharField(max_length=100, null=False)
	padeceEnfermedades = models.CharField(max_length=100, null=False)
	enfermedadTrasmisionSexual = models.CharField(max_length=100, null=False)
	otraEnfermedad = models.CharField(max_length=100, null=False)
	estaEmbarazada = models.CharField(max_length=100, null=False)
	observaciones = models.TextField()
	resumenClinico = models.TextField()

	def __unicode__(self):

		nombres ="%s %s %s %s"% (self.medico,self.paciente,self.observaciones,self.resumenClinico)
		return nombres


class ListadeDiagnosticos(models.Model):
	codigoDiagnostico=models.CharField(max_length=15)
	nombreDiagnostico=models.CharField(max_length=30)
	
	def __unicode__(self):
<<<<<<< HEAD

		codigoCie="%s "%(self.CIE10)
=======
		codigoCie="%s  %s"%(self.codigoDiagnostico,self.nombreDiagnostico)
>>>>>>> e973b9c48f8c7a717c93d81f839415bc97defd98
		return codigoCie

class Odontograma(models.Model):
 	doctor=models.ForeignKey(Medico)
 	paciente=models.ForeignKey(Paciente)
 	fechayHora = models.DateTimeField(blank=True, null=True)
 	nombrePiezaDental=models.CharField(max_length=40)
 	problemaDental=models.ForeignKey(ListadeDiagnosticos)
 	notas=models.TextField()
 	
 	def __unicode__(self):
<<<<<<< HEAD
 		problema="%s  "% (self.problemaDental)
=======
 		problema="%s %s %s"% (self.doctor,self.paciente,self.fechayHora)
>>>>>>> e973b9c48f8c7a717c93d81f839415bc97defd98
 		return problema


