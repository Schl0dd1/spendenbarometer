from django.contrib import admin

from .models import Konto
from .models import Buchung



admin.site.register(Konto)
admin.site.register(Buchung)