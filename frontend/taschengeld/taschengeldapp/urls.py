from django.urls import path
from . import views

app_name = 'taschengeldapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:konto_id>/', views.detail, name='detail'),
    path('<int:konto_id>/neuer_eintrag/', views.neuer_eintrag, name='neuer_eintrag'),
    path('delete_buchung/<int:buchung_id>/', views.delete_buchung, name='delete-buchung'),
    path('neues_konto/', views.neues_konto, name='neues_konto'),
    path('<int:konto_id>/delete_konto/', views.delete_konto, name='delete-konto')
]