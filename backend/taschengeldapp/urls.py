from django.urls import path, include
from . import views
from .api import BuchungResource, KontoResource

app_name = "taschengeldapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:konto_id>/", views.detail, name="detail"),
    path("<int:konto_id>/neuer_eintrag/", views.neuer_eintrag, name="neuer_eintrag"),
    path(
        "delete_buchung/<int:buchung_id>/", views.delete_buchung, name="delete-buchung"
    ),
    path("neues_konto/", views.neues_konto, name="neues_konto"),
    path("api/konten/", include(KontoResource.urls())),
    path("api/buchungen/", include(BuchungResource.urls())),
    # path(
    #     "api/buchungen/<pk>/",
    #     include(BuchungResource.as_detail(), name="api_buchung_detail"),
    # ),
]
