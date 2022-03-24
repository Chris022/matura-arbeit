# Emtfernen von Mustern

## Problem

Damit das Bild in eine Schaltung umgewandelt werden kann, darf es bestimmte Muster in dem Bild der Schaltung nicht geben, da es bei diesen bei der weiteren Verarbeitung der Schaltung zu Fehlern kommen würde.

![Beispiel eines zu Entfernendes Muster](.\Dateien\MusterUndErsatz.png){width=60%} 

## Idee

In dem Bild der Schaltung werden diese bestimmten Muster gesucht und so verändert, dass es später nicht mehr zu Fehlern kommen kann.

## Umsetzung

Jedes Muster welches erestzt werden soll wird in einer Liste gespeichert. In einer weiteren Liste wir das jeweilige Muster gespeichert welches das erste ersetzen soll. 

Danach wird jeder schwarze Pixel im Bild überprüft, ob dieser Pixel sowie die angrenzenden Pixel gleich wie ein zu ersetzendes Muster sind. Wird ein zu ersetzendes Muster gefunden, werden die entsprechenden Pixel im ursprünglichen Bild mit dem zuvor festgelegtem Ersatzmuster ausgetauscht.

![Entfernen eines Musters](.\Dateien\Funktion.png){width=80%} 