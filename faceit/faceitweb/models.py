from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=70)
    first_name = models.CharField(max_length=70, default='')
    last_name = models.CharField(max_length=70, default='')

    def __unicode__(self):              # __unicode__ on Python 2
        return self.full_name
