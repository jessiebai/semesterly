"""
Copyright (C) 2017 Semester.ly Technologies, LLC

Semester.ly is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Semester.ly is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-03-12 00:25
from __future__ import unicode_literals
from operator import attrgetter

from django.db import migrations

from timetable.update_semester_field import get_update_operation

tables_to_update = [
  'PersonalTimetable',
]


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0017_personaltimetable_semester'),
    ]

    operations = [
      migrations.RunPython(get_update_operation('student', 
                                                tables_to_update,
                                                attrgetter('school'))),      
    ]
