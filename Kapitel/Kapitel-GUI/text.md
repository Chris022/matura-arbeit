# GUI

## Problem

Um das Bild in eine Schaltung umwandeln zu können, muss dieses erst in ein Binärbild umgewandelt werden.
Dafür wird ein Algorithmus aus der Python Library OpenCV verwendet. Da jedoch jedes Bild unterschiedlich beleuchtet ist, ist es nicht möglich, bei allen Bildern dieselben Einstellungen zu benutzen.


## Idee

Bei jedem Bild kann der Benutzer selbst gewisse Werte für den Alogrithmus verändern und sieht das jeweilige Ergebnis. So kann jedes Bild in ein optimales Binärbild umgewandelt werden.

## Umsetzung

Die GUI ist in verschidene Abschnitte unterteilt.

* Bild öffnen
* Bild zuschneiden
* Binärbild erstellen
* Bild umwandeln

Mit den Knöpfen "Next" und "Back" kann jederzeit einen Abschnitt nach vorne oder zurück gewechselt werden. 


### Bild öffnen

Wird das Programm gestartet, muss man zuerst ein Bild öffnen.

![Bild öffnen](.\Dateien\OpenFile.png){width=80%}

Wird der Knopf "Open File" gedrückt, öffnet sich in einem neuen Fenster der File Explorer. In diesem kann der PC nach einem Bild durchsucht werden. Mit dem Knopf "Open" wird das gewünschte Bild ausgewählt.

![Bild im File Explorer auswählen](.\Dateien\FileExplorer.png){width=80%}

### Bild zuschneiden

Das ausgewählte Bild wird jetzt im Programm angezeigt und kann noch zugeschnitten werden, damit auf dem Bild nur noch die Schaltung zu sehen ist. Dafür wird mit der Maus auf einen Punkt geklickt und mit gedrückter Maustaste die Maus zu einem zweiten Punkt bewegt. Das dadurch entstehende Rechteck zeigt den Teil des Bildes, welcher ausgeschnitten wird. Der restliche Teil des Bildes wird ausgegraut dargestellt.

![Bild zuschneiden](.\Dateien\CropImage2.png){width=80%}

### Binärbild erstellen

Als nächstes wird das Bild in ein Binärbild umgewandelt. 

Dazu wird eine der zwei Funktionen "threshold" oder "adaptiveThreshold" aus der Library OpenCV verwendet.

Um ein besseres Ergebnis zu erzielen, kann die Funktion "GaussianBlur" mit Hilfe des ersten Schiebereglers "Blur" zusätzlich das Bild unscharf machen, um Rauschen aus dem Bild zu entfernen.

Der Funktion "threshold" wird ein Schwellenwert zwischen 0 und 255 übergeben. Dieser Wert kann mithilfe des zweiten Schiebereglers "Threshold value" eingestellt werden. Jeder Pixel mit einem Wert unter dem Schwellenwert wird auf 0 gesetzt, jeder mit einem höheren Wert auf 255.

Diese funktioniert jedoch nur bei gleichmäßig ausgeleuchteten Bildern.

Das Ergebnis dieser Funktion bei ungleichmäßig ausgeleuchteten Bildern ist in der unteren Abbildung zu sehen.
Für diese Fälle gibt es eine zweite Möglichkeit, ein Bild in ein Binärbild umzuwandeln.
Da die erste Möglichkeit einfacher und schneller zu benutzen ist und bei einem Großteil der Bilder funktioniert, stehen dem Benutzer beide Funktionen zur Verfügung.

![Binärbild erstellen](.\Dateien\SimpleThreshold2.png){width=80%}

\newpage

Die zweite Funktion "adaptiveThreshold" benutzt für jede Bildregion einen anderen Schwellenwert, der von der Beleuchtung in dem jeweiligen Bereich abhängt. Dadurch ist es auch möglich, bei ungleichmäßig ausgeleuchteten Bildern ein Binärbild zu erstellen.
Mit dem dritten und vierten Schieberegler "Block size" und "Constant" können die beiden Parameter für diese Funktion verändert werden.
"Block size" gibt dabei an, wie viele Nachbarpixel zur Berechnung des Schwellenwertes verwendet werden.
"Constant" ist ein Wert, der von dem berechneten Schwellwert subtrahiert wird.


![Binärbild erstellen](.\Dateien\AdaptiveThreshold2.png){width=80%}

Mit dem Knopf "Reset" kann das Bild wieder auf das Ausgangsbild zurückgesetzt werden.

\newpage

### Bild in Schaltung umwandeln

Zuletzt kann die Schaltung mit dem Knopf "Detect Circuit" in ein LTspice File umgewandelt werden.

![Bild umwandeln](.\Dateien\Detect2.png){width=80%}

Wenn die Schaltung fertig umgewandelt wurde, wird LTspice gestarten und die erstellte Datei wird geöffnet. 

![Schaltung in LTSpice](.\Dateien\LTSPice.png){width=80%}