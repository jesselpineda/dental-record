# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cotizacion'
        db.create_table('cotizacion_cotizacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('paciente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['altas.Paciente'], null=True)),
            ('medico', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['altas.Medico'])),
        ))
        db.send_create_signal('cotizacion', ['Cotizacion'])

        # Adding model 'CatalogodeServicios'
        db.create_table('cotizacion_catalogodeservicios', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombreDelServicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ActividadesClinicas.Tratamiento'])),
            ('nombreDelGrupo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['precios.GrupoPrecios'])),
            ('precio', self.gf('django.db.models.fields.DecimalField')(max_digits=19, decimal_places=3)),
        ))
        db.send_create_signal('cotizacion', ['CatalogodeServicios'])

        # Adding model 'CotizacionDetail'
        db.create_table('cotizacion_cotizaciondetail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estado', self.gf('django.db.models.fields.CharField')(default='aceptdado', max_length=10)),
            ('cotizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cotizacion.Cotizacion'])),
            ('servicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cotizacion.CatalogodeServicios'])),
        ))
        db.send_create_signal('cotizacion', ['CotizacionDetail'])


    def backwards(self, orm):
        # Deleting model 'Cotizacion'
        db.delete_table('cotizacion_cotizacion')

        # Deleting model 'CatalogodeServicios'
        db.delete_table('cotizacion_catalogodeservicios')

        # Deleting model 'CotizacionDetail'
        db.delete_table('cotizacion_cotizaciondetail')


    models = {
        'ActividadesClinicas.tratamiento': {
            'Meta': {'object_name': 'Tratamiento'},
            'codigoTratamiento': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreTratamiento': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'altas.medico': {
            'Ciudad': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Meta': {'object_name': 'Medico'},
            'apellidoMaterno': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'apellidoPaterno': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'cedulaEstatal': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'codigoPostal': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'correoElectronico': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'especialidad': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'licenciaDeEspecialidad': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'licenciaMedica': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'nombreUsuario': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'rfc': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'universidadEgreso': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        'altas.paciente': {
            'Meta': {'object_name': 'Paciente'},
            'apellidoMaterno': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'apellidoPaterno': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'codigoPostal': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'correoElectronico': ('django.db.models.fields.EmailField', [], {'max_length': '60'}),
            'credencialPaciente': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precios.GrupoPrecios']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nSs': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'cotizacion.catalogodeservicios': {
            'Meta': {'object_name': 'CatalogodeServicios'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreDelGrupo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['precios.GrupoPrecios']"}),
            'nombreDelServicio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ActividadesClinicas.Tratamiento']"}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '19', 'decimal_places': '3'})
        },
        'cotizacion.cotizacion': {
            'Meta': {'object_name': 'Cotizacion'},
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medico': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['altas.Medico']"}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['altas.Paciente']", 'null': 'True'})
        },
        'cotizacion.cotizaciondetail': {
            'Meta': {'object_name': 'CotizacionDetail'},
            'cotizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cotizacion.Cotizacion']"}),
            'estado': ('django.db.models.fields.CharField', [], {'default': "'aceptdado'", 'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cotizacion.CatalogodeServicios']"})
        },
        'precios.grupoprecios': {
            'Meta': {'object_name': 'GrupoPrecios'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreDelGrupo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['cotizacion']