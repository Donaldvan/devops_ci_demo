# -*- coding: utf-8 -*-
from django.db import models, migrations
import name_tools

def breakout_names(apps, schema_editor):
    User = apps.get_model("faceitweb", "User")
    for user in User.objects.all():
        prefix, first_name, last_name, suffix = name_tools.split(user.full_name)

        user.first_name = first_name
        user.last_name = last_name

        user.save()
def reverse_it(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('faceitweb', '0002_auto_20160512_2128'),
    ]

    operations = [
        migrations.RunPython(breakout_names, reverse_it),
    ]
