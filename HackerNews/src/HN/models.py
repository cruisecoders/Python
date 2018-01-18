# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Hnews(models.Model):
    hn_id = models.IntegerField(default=0, unique=True, null=True)
    username = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    url = models.CharField(max_length=300, null=True)
    score = models.CharField(max_length=150, null=True)
    hn_type = models.CharField(max_length=150, null=True)
    sentiments = models.CharField(max_length=150, null=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
