from django.contrib import admin

from .models import (Person, Connection, Homework, Meeting) 

admin.site.register(Person)
admin.site.register(Connection)
admin.site.register(Homework)
admin.site.register(Meeting)

