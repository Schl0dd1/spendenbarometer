from django.urls import path
from . import views

app_name = 'taschengeldapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:konto_id>/', views.detail, name='detail'),
    path('<int:konto_id>/neuer_eintrag/', views.neuer_eintrag, name='neuer_eintrag'),
]