# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151124_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='comment',
            field=models.ForeignKey(blank=True, to='core.Comment', null=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='trip',
            field=models.ForeignKey(blank=True, to='core.Trip', null=True),
        ),
    ]
