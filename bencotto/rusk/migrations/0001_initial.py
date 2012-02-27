# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'rusk'
        db.create_table('rusk_rusk', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('views', self.gf('django.db.models.fields.IntegerField')()),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('rusk', ['rusk'])

        # Adding model 'rusk_comments'
        db.create_table('rusk_rusk_comments', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rusk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rusk.rusk'])),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('rusk', ['rusk_comments'])


    def backwards(self, orm):
        
        # Deleting model 'rusk'
        db.delete_table('rusk_rusk')

        # Deleting model 'rusk_comments'
        db.delete_table('rusk_rusk_comments')


    models = {
        'rusk.rusk': {
            'Meta': {'object_name': 'rusk'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'views': ('django.db.models.fields.IntegerField', [], {})
        },
        'rusk.rusk_comments': {
            'Meta': {'object_name': 'rusk_comments'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rusk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rusk.rusk']"})
        }
    }

    complete_apps = ['rusk']
