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
        return Buchung.objects.create(
            konto=self.data["kontoId"], betrag=self.data["betrag"]
        )

    def delete(self, pk):
        Buchung.objects.get(id=pk).delete()


class KontoResource(DjangoResource):
    preparer = FieldsPreparer(
        fields={
            "id": "id",
            "kontoname": "konto_name",
            "kontostand": "aktueller_kontostand",
        }
    )

    def detail(self, pk):
        konto = Konto.objects.get(pk=pk)
        return konto

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

        konto.konto_name = self.data["kontoname"]
        konto.save()
        return konto

    def delete(self, pk):
        Konto.objects.get(id=pk).delete()
