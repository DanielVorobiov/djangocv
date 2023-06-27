from django.contrib import admin

from cv.models import Achievement, Education, Experience, Person

# Register your models here.

admin.site.register([Person, Experience, Education, Achievement])
