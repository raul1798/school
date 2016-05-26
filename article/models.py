# -*- coding: utf-8 -*-
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


	class Meta:
		verbose_name = u"Новость"
		verbose_name_plural = u"Новости"

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

	class Meta:
		verbose_name = u"Фото для новости"
		verbose_name_plural = u"Фото для новости"

	def __unicode__(self):
		return u'%s' % self.article

class Zno(models.Model):
	title = models.CharField(max_length=90)

	class Meta:
		verbose_name = u"ЗНО"
		verbose_name_plural = u"ЗНО"

	def __unicode__(self):
		return u'%s' % self.title


class ZnoDoc(models.Model):
	doc = models.ForeignKey(Zno, null=True)
	file = models.FileField(upload_to='media', null=True)

	def filename(self):
		return os.path.basename(self.file.name)

	class Meta:
		verbose_name = u"Документ для ЗНО"
		verbose_name_plural = u"Документы для ЗНО"

	def __unicode__(self):
		return u'%s' % self.doc
		


class Dpa(models.Model):
	title = models.CharField(max_length=90)

	class Meta:
		verbose_name = u"ДПА"
		verbose_name_plural = u"ДПА"

	def __unicode__(self):
		return u'%s' % self.title


class DpaDoc(models.Model):
	doc = models.ForeignKey(Dpa, null=True)
	file = models.FileField(upload_to='media', null=True)

	def filename(self):
		return os.path.basename(self.file.name)

	class Meta:
		verbose_name = u"Документ для ДПА"
		verbose_name_plural = u"Документы для ДПА"

	def __unicode__(self):
		return u'%s' % self.doc



class Vchitel(models.Model):
	title = models.CharField(max_length=90)

	class Meta:
		verbose_name = u"Учителю"
		verbose_name_plural = u"Учителю"

	def __unicode__(self):
		return u'%s' % self.title



class VchitelDoc(models.Model):
	doc = models.ForeignKey(Vchitel, null=True)
	file = models.FileField(upload_to='media', null=True)

	def filename(self):
		return os.path.basename(self.file.name)

	class Meta:
		verbose_name = u"Документ учителю"
		verbose_name_plural = u"Документы учителю"

	def __unicode__(self):
		return u'%s' % self.doc



class Klassam(models.Model):
	title = models.CharField(max_length=90,verbose_name='Класс' )

	class Meta:
		verbose_name = u"Классам"
		verbose_name_plural = u"Классам"

	def __unicode__(self):
		return u'%s' % self.title


class KlassamDoc(models.Model):
	doc = models.ForeignKey(Klassam, null=True, verbose_name='К какому классу')
	file = models.FileField(upload_to='media', null=True, verbose_name='Документ')

	def filename(self):
		return os.path.basename(self.file.name)

	class Meta:
		verbose_name = u"Документы классам"
		verbose_name_plural = u"Документы классам"

	def __unicode__(self):
		return u'%s' % self.doc

	
		


	
		



	
		
