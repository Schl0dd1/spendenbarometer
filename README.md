# taschengeldapp
<br />Dokumentation: 
<br />Es wurden 2 model (Konto und Buchung) angelegt. Jede Buchung ist mit dem Key eines Kontos verknüpft.
<br />Model 'Konto' beinhaltet Name, Inhaber*in, aktueller Kontostand, erstellungsdatum
<br />Model 'Buchung' beinhaltet Konto(Foreign key), beschreibung, betrag, ausgabe/einnahme(BooleanField False=ausgabe, True=einnahme)
<br />das Formular bekommt die daten aus dem Model übergeben und speichert die einträge in der datenbank (am ende sollen aber nicht alle felder ausgefüllt werden müssen)

<br />nächste Schritte:
- customize admin page
- form überarbeiten (felder wie datum / konto automatisch füllen)
- projektstruktur korrekturen(wo liegt welche datei richtig)
- weniger views, benutzerfreundlichkeit
