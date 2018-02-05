# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	creado_fecha = models.DateTimeField(default=timezone.now)
	publicado_fecha = models.DateTimeField(blank=True, null=True)
	
	def publish(self):
		self.publicado_fecha = timezone.now()
		self.save()

	def __str__(self):
		return self.title
	
