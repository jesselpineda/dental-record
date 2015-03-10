# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HistoriaClinica'
        db.create_table('ActividadesClinicas_historiaclinica', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('paciente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['altas.Paciente'])),
            ('medico', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['altas.Medico'])),
            ('credencialPaciente', self.gf('django.db.models.fields.CharField')(max_length=15, null=True)),
            ('herenciaMadre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('herenciaPadre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('herenciaHermanos', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('herenciaHijos', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('herenciaEsposos', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('herenciaTios', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('herenciaAbuelos', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('eInflamatoriasnotopciones', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('ets', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('eDegenerativas', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('eNeoplasticas', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('eCongenitas', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('otras', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('habitosHigienicosVest', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('habitosHigienicosCorp', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('frecuenciaLavadoDental', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('uxiliaresBucales', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('consumodeGolosinas', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('gruposanguineo', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('factorRh', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('cartilladeVacunacion', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('esquemaCompleto', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('esquemaFalta', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('adicciones', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('alergias', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('fechaHospitalizaion', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('motivo', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('padecimientoActual', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('aparatoDigestivo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('aparatoRespiratorio', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('aparatoCardioBascular', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('apararoGenitourinario', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('sistemaEndocrina', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('sistemaHemopoyetico', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('sistemamusculoEsqueletico', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('aparatoTegumentario', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('habitusExterior', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('peso', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('talla', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('complexion', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('frecuenciaCardiaca', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('tensionarterial', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('frecuenciaRespiratoria', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('temperatura', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('cabeza', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
            ('craneo', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('caraAsimetria', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('perfil', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('piel', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('musculos', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('cuello', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('otros', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('ruidos', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('chasquidos', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('crepitacion', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('difparaAbrirlaboca', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('dolorabertura', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('fatigadolormuscular', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('disminuciondelaavertura', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('desviacionaverturadecierre', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('ganglios', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('glandulassalivales', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('labioExterno', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('bordebermellon', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('labiointerno', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('Comisuras', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('carrillos', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('fondodesaco', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('frenillos', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('lenguaTerciomedio', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('paladarDuro', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('paladarBlando', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('istmoBucofaringe', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('lenguaDorso', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('lenguaBordes', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('lenguaVentral', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('pisodelaBoca', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('dientes', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('mucosadelBordealveolar', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('encia', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('gingivitis', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('periodontitis', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('receciongingival', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('bolsasperiodontales', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('movilidadDentario', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('indicedeplaca', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('interpretacionradiografica', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('estudiosdeLaboratorio', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('interpretacionEstudiosLaboratorio', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('ActividadesClinicas', ['HistoriaClinica'])

        # Adding model 'Odontograma'
        db.create_table('ActividadesClinicas_odontograma', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('doctor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['altas.Medico'], null=True)),
            ('paciente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['altas.Paciente'], null=True)),
            ('fechayHora', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('notas', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('ActividadesClinicas', ['Odontograma'])

        # Adding model 'Tratamiento'
        db.create_table('ActividadesClinicas_tratamiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigoTratamiento', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('nombreTratamiento', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('ActividadesClinicas', ['Tratamiento'])

        # Adding model 'Procedimiento'
        db.create_table('ActividadesClinicas_procedimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pieza', self.gf('django.db.models.fields.IntegerField')()),
            ('cara', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('tratamiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ActividadesClinicas.Tratamiento'], null=True)),
            ('odontograma', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ActividadesClinicas.Odontograma'], null=True)),
        ))
        db.send_create_signal('ActividadesClinicas', ['Procedimiento'])


    def backwards(self, orm):
        # Deleting model 'HistoriaClinica'
        db.delete_table('ActividadesClinicas_historiaclinica')

        # Deleting model 'Odontograma'
        db.delete_table('ActividadesClinicas_odontograma')

        # Deleting model 'Tratamiento'
        db.delete_table('ActividadesClinicas_tratamiento')

        # Deleting model 'Procedimiento'
        db.delete_table('ActividadesClinicas_procedimiento')


    models = {
        'ActividadesClinicas.historiaclinica': {
            'Comisuras': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'Meta': {'object_name': 'HistoriaClinica'},
            'adicciones': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'alergias': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'apararoGenitourinario': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'aparatoCardioBascular': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'aparatoDigestivo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'aparatoRespiratorio': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'aparatoTegumentario': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'bolsasperiodontales': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'bordebermellon': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'cabeza': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'caraAsimetria': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'carrillos': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'cartilladeVacunacion': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'chasquidos': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'complexion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'consumodeGolosinas': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'craneo': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'credencialPaciente': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'crepitacion': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'cuello': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'desviacionaverturadecierre': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'dientes': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'difparaAbrirlaboca': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'disminuciondelaavertura': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'dolorabertura': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'eCongenitas': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'eDegenerativas': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'eInflamatoriasnotopciones': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'eNeoplasticas': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'encia': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'esquemaCompleto': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'esquemaFalta': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'estudiosdeLaboratorio': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'ets': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'factorRh': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'fatigadolormuscular': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'fechaHospitalizaion': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'fondodesaco': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'frecuenciaCardiaca': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'frecuenciaLavadoDental': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'frecuenciaRespiratoria': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'frenillos': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'ganglios': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'gingivitis': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'glandulassalivales': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'gruposanguineo': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'habitosHigienicosCorp': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'habitosHigienicosVest': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'habitusExterior': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'herenciaAbuelos': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'herenciaEsposos': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'herenciaHermanos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'herenciaHijos': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'herenciaMadre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'herenciaPadre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'herenciaTios': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicedeplaca': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'interpretacionEstudiosLaboratorio': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'interpretacionradiografica': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'istmoBucofaringe': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'labioExterno': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'labiointerno': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'lenguaBordes': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'lenguaDorso': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'lenguaTerciomedio': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'lenguaVentral': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'medico': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['altas.Medico']"}),
            'motivo': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'movilidadDentario': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'mucosadelBordealveolar': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'musculos': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'otras': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'otros': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['altas.Paciente']"}),
            'padecimientoActual': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'paladarBlando': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'paladarDuro': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'perfil': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'periodontitis': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'peso': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'piel': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'pisodelaBoca': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'receciongingival': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'ruidos': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'sistemaEndocrina': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sistemaHemopoyetico': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sistemamusculoEsqueletico': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'talla': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'temperatura': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'tensionarterial': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'uxiliaresBucales': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'})
        },
        'ActividadesClinicas.odontograma': {
            'Meta': {'object_name': 'Odontograma'},
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['altas.Medico']", 'null': 'True'}),
            'fechayHora': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notas': ('django.db.models.fields.TextField', [], {}),
            'paciente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['altas.Paciente']", 'null': 'True'})
        },
        'ActividadesClinicas.procedimiento': {
            'Meta': {'object_name': 'Procedimiento'},
            'cara': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'odontograma': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ActividadesClinicas.Odontograma']", 'null': 'True'}),
            'pieza': ('django.db.models.fields.IntegerField', [], {}),
            'tratamiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ActividadesClinicas.Tratamiento']", 'null': 'True'})
        },
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
        'precios.grupoprecios': {
            'Meta': {'object_name': 'GrupoPrecios'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreDelGrupo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['ActividadesClinicas']