# seminars/admin.py
from django.contrib import admin
from seminars.models import Seminar, Application

admin.site.register(Seminar)
admin.site.register(Application)
