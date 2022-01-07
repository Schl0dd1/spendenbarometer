from django.shortcuts import get_object_or_404, render
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


def detail(request,konto_id):
    konto = get_object_or_404(Konto, pk=konto_id)
    return render(request, 'taschengeldapp/detail.html', {'konto' : konto})

#Übersicht ausgewähltes Konto
def neuer_eintrag(request,konto_id):
    konto = get_object_or_404(Konto, pk=konto_id)
    submitted = False
    if request.method == "POST":
        form = NeuerEintrag(request.POST)   
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = NeuerEintrag
        if 'submitted' in request.GET:
            submitted = True
        

    args = {'konto': konto, 'form':form, 'submitted':submitted}
    return render(request, 'taschengeldapp/neuer_eintrag.html', args)
  
    
    # submitted = False
    # if request.method == "POST":
    #     form = NeuerEintrag(request.POST)
   
            
   
    # return render(request, 'taschengeldapp/detail.html', args)

#formulareintrag als neue buchung-instanz speichern:
# def neuereintrag(request):
#     form = NeuerEintrag
#     context = {'konto': konto, 'form':form}
#     return render(request, 'taschengeldapp/detail.html', context)









#def speichern(request, konto_id):
#     konto = get_object_or_404(Konto, pk=konto_id)
#     try:
#         b = buchung_set.create(pk=request.POST['konto'], beschreibung='', betrag='',einnahme=False, buchungsdatum=timezone.now())

#         except (KeyError, b.betrag.DoesNotExist):
#             # Redisplay the question voting form.
#             return render(request, 'polls/detail.html', {
#                 'question': question,
#                 'error_message': "Bitte gebe einen Betrag ein",
#             })
#     else:
#         konto.aktueller_kontostand += buchung.betrag
#         buchung.save()

 #    return HttpResponseRedirect(reverse('taschengeldapp:index', args=('',)) )   