from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import NeuerEintrag, NeuesKonto
from django.urls import reverse



#Übersicht alle Konten
def index(request):
    alle_konten = Konto.objects.order_by('-konto_erstellungsdatum')
    context = {
        'alle_konten': alle_konten,
    }
    return render(request, 'taschengeldapp/index.html', context)

#übersicht aller buchungen
def detail(request,konto_id):
    konto = get_object_or_404(Konto, pk=konto_id)
    return render(request, 'taschengeldapp/detail.html', {'konto' : konto})

#NEEDS FIXING:
def delete_buchung(request, buchung_id):
    buchung = Buchung.objects.get(pk=buchung_id)
    #konto = buchung.objects.get(konto) # wie spreche ich das konto an? konto-id mit übergeben? wie?
    #konto.aktueller_kontostand -= buchung.betrag
    #konto.save()
    args = [konto.id]

    buchung.delete()
    return HttpResponseRedirect(reverse('detail', args))

def delete_konto(request, konto_id):
     konto = get_object_or_404(Konto, pk=konto_id)
     konto.delete()
     return HttpResponseRedirect('/')

#NEEDS FIXING
def neues_konto(request):
    if request.method == "POST":
        form = NeuesKonto(request.POST)
        if form.is_valid():
            form.save()
            #how to get id from new account?
            return render(request, 'taschengeldapp/detail.html', {'form' : form})
    else:
        form = NeuesKonto
        if 'submitted' in request.GET:
            submitted = True

    args = {'konto': konto, 'form':form, 'submitted':submitted}
    return render(request, 'taschengeldapp/index.html', args)


#NEEDS FIXING
#Übersicht ausgewähltes Konto
def neuer_eintrag(request,konto_id):
    konto = get_object_or_404(Konto, pk=konto_id)
    submitted = False
    if request.method == "POST":
        form = NeuerEintrag(request.POST)   
        if form.is_valid():
            form.save()
            betrag = form.cleaned_data['betrag']
            konto.aktueller_kontostand += int(betrag)
            konto.save()
            #empty form
            return render(request, 'taschengeldapp/detail.html', {'konto' : konto})
    else:
        form = NeuerEintrag
        if 'submitted' in request.GET:
            submitted = True
        

    args = {'konto': konto, 'form':form, 'submitted':submitted}
    return render(request, 'taschengeldapp/neuer_eintrag.html', args)
  
    






 