from django.db import models


class Konto(models.Model):
    class Meta:
        verbose_name_plural = "Konten"

    konto_name = models.CharField(max_length=100)
    aktueller_kontostand = models.DecimalField(
        default=0, max_digits=5, decimal_places=2
    )
    konto_erstellungsdatum = models.DateTimeField(auto_now=True)

    def calc_kontostand(self):
        einnahmen = sum([buchung.betrag for buchung in self.buchungen.all() if buchung.einnahme == True])
        ausgaben = sum([buchung.betrag for buchung in self.buchungen.all() if buchung.einnahme == False])
        self.aktueller_kontostand = einnahmen - ausgaben
        self.save()


    def __str__(self):
        return self.konto_name


class Buchung(models.Model):
    class Meta:
        verbose_name_plural = "Buchungen"

    konto = models.ForeignKey(Konto, on_delete=models.CASCADE, related_name="buchungen")
    beschreibung = models.CharField(max_length=200, default="")
    betrag = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    einnahme = models.BooleanField(default=False)
    buchungsdatum = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.beschreibung

    def letzte_buchungen(self):
        return self.buchungsdatum >= timezone.now() - datetime.timedelta(days=7)

    def delete(self, *args, **kwargs):
        konto = Konto.objects.get(id=self.konto_id)
        super(Buchung, self).delete(*args, **kwargs)
        konto.calc_kontostand()

    def save(self, *args, **kwargs):
        super(Buchung, self).save(*args, **kwargs)
        self.konto.calc_kontostand()
