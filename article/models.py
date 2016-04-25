from django.db import models
from datetime import datetime
from django.contrib import admin
from django.conf import settings
from ckeditor.fields import RichTextField
import os


# Create your models here.

# def upload_location(article, filename):
# 	return"%s/%s" %(article.pk, filename)


class Article(models.Model):
	title = models.CharField(max_length=90)
	text = models.TextField(max_length=90000)
	pub_date = models.DateTimeField('Date publication', default=datetime.now)

	def __unicode__(self):
		return u'%s' % self.title

	
class ArticleImage(models.Model):
	article = models.ForeignKey(Article, null=True)
	#adminImage = models.ForeignKey(Administacia, null=True)
	image = models.ImageField(upload_to='media',
		null=True,
		blank=True) 
		# width_field="width_field",
		# height_field="height_field"
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)

	def __unicode__(self):
		return u'%s' % self.article

class Zno(models.Model):
	title = models.CharField(max_length=90)

	def __unicode__(self):
		return u'%s' % self.title


class ZnoDoc(models.Model):
	doc = models.ForeignKey(Zno, null=True)
	file = models.FileField(upload_to='media', null=True)

	def filename(self):
		return os.path.basename(self.file.name)

	def __unicode__(self):
		return u'%s' % self.doc
		

	
class History(models.Model):
	title = models.CharField(max_length=90)
	text = models.TextField(max_length=9000)
	pub_date = models.DateTimeField('Date publication', default=datetime.now)

	def __unicode__(self):
		return u'%s' % self.title


class HistoryImage(models.Model):
	article = models.ForeignKey(History, null=True)
	image = models.ImageField(upload_to='media',
		null=True,
		blank=True) 

	def __unicode__(self):
		return u'%s' % self.article


class Dpa(models.Model):
	title = models.CharField(max_length=90)

	def __unicode__(self):
		return u'%s' % self.title


class DpaDoc(models.Model):
	doc = models.ForeignKey(Dpa, null=True)
	file = models.FileField(upload_to='media', null=True)

	def filename(self):
		return os.path.basename(self.file.name)

	def __unicode__(self):
		return u'%s' % self.doc



class Vchitel(models.Model):
	title = models.CharField(max_length=90)

	def __unicode__(self):
		return u'%s' % self.title


class VchitelDoc(models.Model):
	doc = models.ForeignKey(Dpa, null=True)
	file = models.FileField(upload_to='media', null=True)

	def filename(self):
		return os.path.basename(self.file.name)

	def __unicode__(self):
		return u'%s' % self.doc

	
		


	
		



	
		
