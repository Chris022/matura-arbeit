# Entfernen von Mustern

## Problem

Damit das Bild in eine Schaltung umgewandelt werden kann, darf es bestimmte Muster in dem Bild der Schaltung nicht geben, da es bei diesen bei der weiteren Verarbeitung der Schaltung zu Fehlern kommen würde. Zu welchen Fehlern diese Mustern führen würden, wird im Kapitel "Umwandeln der Schaltung in eine Graph Datenstruktur" erklärt.

![Beispiel eines zu entfernenden Musters](.\Dateien\MusterUndErsatz.png){width=60%} 

## Idee

In dem Bild der Schaltung werden diese bestimmten Muster gesucht und so verändert, dass es später nicht mehr zu Fehlern kommen kann.

## Umsetzung

Jedes Muster, welches ersetzt werden soll, wird in einer Liste gespeichert. In einer weiteren Liste wird das jeweilige Muster gespeichert, welches das erste ersetzen soll. 

Danach wird jedes schwarze Pixel im Bild überprüft, ob dieses Pixel sowie die angrenzenden Pixel gleich wie ein zu ersetzendes Muster sind. Wird ein zu ersetzendes Muster gefunden, werden die entsprechenden Pixel im ursprünglichen Bild mit dem zuvor festgelegtem Ersatzmuster ausgetauscht.

![Entfernen eines Musters](.\Dateien\Funktion.png){width=80%} 