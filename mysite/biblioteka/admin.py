from django.contrib import admin

from .models import Gatunek,Czytelnicy, Ksiazka

admin.site.register(Gatunek)
admin.site.register(Czytelnicy)
admin.site.register(Ksiazka)