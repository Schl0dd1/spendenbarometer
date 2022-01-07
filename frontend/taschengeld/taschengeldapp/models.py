

from django.db import models


class Konto(models.Model):
    konto_name = models.CharField(max_length=100)
    aktueller_kontostand = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    konto_erstellungsdatum = models.DateTimeField('erstellt am')
    
    def __str__(self):
        return self.konto_name

class Buchung(models.Model):
    konto = models.ForeignKey(Konto, on_delete=models.CASCADE)
    beschreibung = models.CharField(max_length=200)
    betrag = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    einnahme = models.BooleanField(default=False)
    buchungsdatum = models.DateTimeField('erstellt am')
    
    def __str__(self):
        return self.beschreibung
    
    def letzte_buchungen(self):
        return self.buchungsdatum >= timezone.now() - datetime.timedelta(days=7)

        




    

