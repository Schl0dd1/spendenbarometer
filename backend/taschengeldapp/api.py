from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer, SubPreparer
from restless.resources import skip_prepare
from .models import Konto


class KontoResource(DjangoResource):
    preparer = FieldsPreparer(
    fields={
    "id": "id",
    "kontoname": "konto_name",
    "kontostand":"aktueller_kontostand"

    }
    )
    def detail(self, pk):
        konto =Konto.objects.get(pk=pk)
        return  konto

    

    def is_authenticated(self):
        return self.request.user.is_authenticated

    def list(self):
        return Konto.objects.all()