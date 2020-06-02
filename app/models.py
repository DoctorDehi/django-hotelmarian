from django.db import models


# Create your models here.
class Pokoj(models.Model):
    nazev = models.CharField(max_length=128)
    pocet_luzek = models.IntegerField()
    cena = models.IntegerField()
    popis = models.CharField(max_length=1024)

    class Meta:
        verbose_name_plural = 'Pokoje'

    def __str__(self):
        return self.nazev

class ObrazekPokoje(models.Model):
    obrazek_url = models.CharField(max_length=256)
    pokoj = models.ForeignKey('Pokoj', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Obrázky pokojů'

class Rezervace(models.Model):
    pokoj = models.ForeignKey('Pokoj', on_delete=models.CASCADE)
    pocet_noci = models.IntegerField()
    jmeno = models.CharField(max_length=100)
    adresa = models.CharField(max_length=200)
    datum_prijezdu = models.DateField()
    datum_odjezdu = models.DateField()

    def __str__(self):
        return "Rezervace číslo %s" % self.id

    class Meta:
        verbose_name_plural = 'Rezervace'