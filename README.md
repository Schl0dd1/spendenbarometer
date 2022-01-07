# taschengeldapp
<br />Offene Fragen: wo muss sich das django-project befinden? Momentan befindet es sich im Frontend-Ordner

## Dokumentation: 
<br />Es wurden 2 model (Konto und Buchung) angelegt. Jede Buchung ist mit dem Key eines Kontos verknüpft.
<br />Model 'Konto' beinhaltet Name, Inhaber*in, aktueller Kontostand, erstellungsdatum
<br />Model 'Buchung' beinhaltet Konto(Foreign key), beschreibung, betrag, ausgabe/einnahme(BooleanField False=ausgabe, True=einnahme)
<br />das Formular bekommt die daten aus dem Model übergeben und speichert die einträge in der datenbank (am ende sollen aber nicht alle felder ausgefüllt werden müssen)

## nächste Schritte:
- delete-button hinzufügen
- form überarbeiten (felder wie datum / konto automatisch füllen)
- fix einnahme-checkbox ->switch-between einnahme ausgabe
- customize admin page
- projektstruktur korrekturen(wo liegt welche datei richtig)
- weniger views, benutzerfreundlichkeit
- konto anlegen/löschen

