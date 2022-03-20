# GUI

## Problem

Um das Bild in eine Schaltung umwandeln zu können, muss dieses erst in ein Binärbild umgewandelt werden.
Dafür wird ein Algorithmus aus der Python Library OpenCV verwendet. Da jedoch jedes Bild unterschiedlich beleuchtet ist, ist es nicht möglich bei allen Bildern die selben Einstellungen zu benutzen.


## Idee

Bei jedem Bild kann der Benutzer selbst gewisse Werte für den Alogrithmus verändern und sieht das jeweilige Ergebnis. So kann jedes Bild in ein optimales Binärbild umgewandelt werden.

## Umsetzung

Die GUI ist in verschiedene Fenster unterteilt. Jedes dieser Fenster ist für einen Teil zuständig. Mit den Knöpfen "Next" und "Back" kann jederzeit ein Fenster nach vorne oder zurück gewechselt werden. 

### Bild öffnen

Wird das Programm gestartet, muss mann zuerst ein Bild öffnen.

![Bild öffnen](.\Dateien\OpenFile.png){width=80%}

Wird der Knopf "Open File" gedrückt, öffnet sich in einem neuen Fenster der File Explorer. In diesem kann der PC nach einem Bild durchsucht werden. Mit dem Knopf "Open" wird das gewünschte Bild ausgewählt.

![Bild im File Explorer auswählen](.\Dateien\FileExplorer.png){width=80%}

### Bild zuschneiden

Das Ausgewählte Bild wird jetzt im Program angezeigt und kann noch zugeschnitten werden, damit auf dem Bild nur noch die Schaltung zu sehen ist. Dafür wird mit der Maus auf einen Punkt geklickt und mit gedrückter Maustaste die Maus zu einem zweiten Punkt bewegt. Das dadurch entstehende Rechteck zeigt den Teil des Bildes, welcher ausgeschnitten wird. Der restliche Teil des Bildes wird ausgegraut dargestellt.

![Bild zuschneiden](.\Dateien\CropImage.png){width=80%}

### Binärbild erstellen

Als nächstes wird das Bild in ein Binärbild umgewandelt. 

Dazu wird eine der zwei Funktionen "threshold" oder "adaptiveThreshold" aus der Library OpenCV verwendet.

Der Funktion "threshold" wird ein Schwellenwert zwischen 0 und 255 übergeben. Diser Wert kann mithilfe des zweiten Schiebereglers eingestellt werden. Jeder Pixel mit einem Wert unter dem Schwellenwert wird auf 0 gesetzt, jeder mit einem höheren Wert auf 255.
Um ein besseres Ergebnis zu erzielen, kann mit dem ersten Schieberegler zusätzlich diie Funktion "GaussianBlur" das Bild unscharf machen, um Rauschen aus dem Bild zu entfernen.

Diese funktioniert jedoch nur bei gleichmäßig ausgeleuchteten Bildern.

Das Ergebniss dieser Funktion bei ungleichmäßig ausgeleuchteten Bildern ist in der unteren Abbildung zu sehen.
Für diese Fälle gibt es eine zweite Möglichkeit ein Bild in ein Binärbild umzuwandeln.

![Binärbild erstellen](.\Dateien\SimpleThreshold.png){width=80%}

Die zweite Funktion "adaptiveThreshold" benutzt für jede Bildregion einen anderen Schwellenwert der von der Beleuchtung in dem jeweiligen Bereich abhängt. Dadurch ist es auch möglich bei ungleichmäßig ausgeleuchteten Bildern ein Binärbild zu erstellen.
Mit dem vierten und fünften Schieberegler können die beiden Parameter für diese Funktion verändert werden.
Wie bei der ersten Methode kann auch wieder hier mit dem dritten Schiebergeler das Bild unscharf gemacht werden, um ein besseres Ergebnis zu erzielen.


![Binärbild erstellen](.\Dateien\AdaptiveThreshold.png){width=80%}

Mit dem Knopf "Reset" kann das Bild wieder auf das Ausgangsbild zurückgesetzt werden.


### Bild in Schaltung umwandeln

Zuletzt kann die Schaltung mit dem Knopf "Detect Circuit" in ein LTspice File umgewandelt werden.

![Bild umwandeln](.\Dateien\Detect.png){width=80%}

Wenn die Schaltung fertig umgewandelt wurde, wird LTspice gestarten und die erstellte Datei wird geöffnet. 

![Schaltung in LTSpice](.\Dateien\LTSPice.png){width=80%}