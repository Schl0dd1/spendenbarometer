from dataclasses import field, fields
from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer, SubPreparer
from restless.resources import skip_prepare
from .models import Buchung, Konto


class BuchungResource(DjangoResource):
    preparer = FieldsPreparer(
        fields={
            "id": "id",
            "kontoId": "konto.id",
            "beschreibung": "beschreibung",
            "betrag": "betrag",
            "einnahme": "einnahme",
            "buchungsdatum": "buchungsdatum",
        }
    )

    def detail(self, pk):
        buchung = Buchung.objects.get(id=pk)
        return buchung

    def is_authenticated(self):
        # return self.request.user.is_authenticated
        return True

    def list(self):
        return Buchung.objects.all()

    def create(self):
        print(self.data)
        return Buchung.objects.create(
            konto=Konto.objects.get(id=self.data["data"]["kontoId"]),
            betrag=self.data["data"]["betrag"],
            einnahme=self.data["data"]["einnahme"],
        )

    def delete(self, pk):
        Buchung.objects.get(id=pk).delete()


class KontoResource(DjangoResource):
    preparer = FieldsPreparer(
        fields={
            "id": "id",
            "kontoname": "konto_name",

        }
    )

    @skip_prepare
    def detail(self, pk):

        konto = Konto.objects.get(pk=pk)
        buchungen = Buchung.objects.filter(konto_id=konto.id)
        # buchungen = Buchung.objects.filter(konto=konto) same like 57
        # buchungen = konto.buchungen.all() same like 57
        return {
            "id": konto.id,
            "kontoname": konto.konto_name,
            "buchungen": [{
                "id": b.id,
                "betrag": b.betrag,
                "beschreibung": b.beschreibung,
                "einnahme": b.einnahme,
            } for b in buchungen],
        }

    def is_authenticated(self):
        # return self.request.user.is_authenticated
        return True

    def list(self):
        return Konto.objects.all()

    def create(self):
        print(self.data)
        return Konto.objects.create(konto_name=self.data["data"]["kontoname"])

    def update(self, pk):
        try:
            konto = Konto.objects.get(id=pk)
        except Konto.DoesNotExist:
            konto = Konto()

        konto.aktueller_kontostand = self.data["data"]["kontostand"]
        konto.save()
        return konto

    def delete(self, pk):
        Konto.objects.get(id=pk).delete()
