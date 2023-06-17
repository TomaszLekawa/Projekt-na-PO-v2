from django.db import models


class Gatunek(models.Model):
    nazwa_gatunku = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa_gatunku

class Czytelnicy(models.Model):
    id_czytelnika = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=100)

    def __str__(self):
        return self.id_czytelnika
    def __str__(self):
        return self.imie

class Ksiazka(models.Model):
    id_ksiazki = models.AutoField(primary_key=True)
    tytul_ksiazki = models.CharField(max_length=100)
    gatunek = models.ForeignKey(Gatunek, on_delete=models.CASCADE)
    czytali = models.ForeignKey(Czytelnicy, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_ksiazki
    def __str__(self):
        return self.tytul_ksiazki
    def __str__(self):
        return self.gatunek
    def __str__(self):
        return self. czytali