from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import NeuerEintrag



#Übersicht alle Konten
def index(request):
    alle_konten = Konto.objects.order_by('-konto_erstellungsdatum')
    template = loader.get_template('taschengeldapp/index.html')
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
    konto = buchung.objects.get(konto_id)
    buchung.delete()
    return redirect ('detail')

def delete_konto(request, konto_id):
     konto = get_object_or_404(Konto, pk=konto_id)
     konto.delete()
     return index(request)

#NEEDS FIXING
def neues_konto(request):
    if request.method == "POST":
        form = NeuesKonto(request.POST)
        if form.is_valid():
            konto_name = form.cleaned_data['name']
            k = Konto(konto_name=konto_name)
            k.save()

            return HttpResponseRedirect('?submitted=True')
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
            konto.betrag += int(betrag)
            return HttpResponseRedirect('?submitted=True')
    else:
        form = NeuerEintrag
        if 'submitted' in request.GET:
            submitted = True
        

    args = {'konto': konto, 'form':form, 'submitted':submitted}
    return render(request, 'taschengeldapp/neuer_eintrag.html', args)
  
    






 