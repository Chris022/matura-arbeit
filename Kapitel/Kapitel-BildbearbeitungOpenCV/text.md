# Bildbearbeitung mit OpenCV

## Problem

Um das Bild der Schaltung weiter verarbeiten zu können, ist es wichtig, alle Linien in dem Bild der Schaltung auf eine Breite von einem Pixel zu verändern.

## Idee

Mithilfe der Funktion "ximgproc.thinning" aus der Python Library OpenCV soll jede Linie in dem Bild in eine Linie mit einer Breite von einem Pixel umgewandelt werden.

![Binärbild und gewünschtes Ergebnis](.\Dateien\Ziel.png){width=100%}

### Problem bei Spulen

Dieser Algorithmus funktioniert jedoch bei Spulen nicht, da diese für den Algorithmus nur eine breitere Linie, wie die Verbindungen zwischen den Bauteilen, darstellen und somit auch zu einer ein Pixel breiten Linie geändert werden.

![Problem bei Spulen](.\Dateien\problemSpulen.png){width=100%}

\newpage

### Lösung für Spulen

Um zu verhindern dass Spulen entfernt werden, werden zuerst die schwarzen Flächen in den Spulen entfernt. Spulen haben somit die gleiche Struktur wie Widerstände und können in eine ein Pixel breite Linie umgewandelt werden.

![Lösung für Spulen](.\Dateien\lösungSpulen.png){width=100%}

## Umsetzung

### Durchschnittliche Dicke einer Linie

Um Spulen entfernen zu können, muss zuerst die durchschnittliche Dicke der Linien in der Schaltung herausgefunden werden.

Dafür wird in jeder Spalte jedes Pixel nacheinander überprüft. Sobald ein Pixel schwarz ist, hat man eine Linie gefunden. Ein Zähler wird ab diesem Pixel so lange erhöht, bis wieder ein weißer Pixel auftritt und die gezeichnete Linie somit endet. Nach jeder Linie wird die Dicke der Linie in dieser Spalte in eine Liste gespeichert. 

Beispiel einer Linie, welche in der rot makierten Spalte drei Pixel breit ist.

![Liniendicke in einer Spalte](.\Dateien\lineThick.png){width=40%}

Als durchschnittliche Liniendicke wird der Wert gewählt, welcher bei den in der Liste gespeicherten Breiten am häufigsten auftritt.


\newpage

### Beispiel der Funktion Erode

Um Spulen zu entfernen, wird die Funktion "erode" aus der Library OpenCV verwendet. Dabei wird eine Filtermaske über ein Bild geschoben. Ein Pixel im Originalbild bleibt nur dann weiß, wenn alle Pixel unter dem Filter weiß sind.

![Funktion "erode" mit 3x3 Filter Beispiel 1](.\Dateien\erode1.png){width=60%}

Unter dem 3x3 Filter sind schwarze und weiße Pixel, somit wird das Pixel im Zentrum des Filters schwarz.

![Funktion "erode" mit 3x3 Filter Beispiel 2](.\Dateien\erode2.png){width=60%}

Wird der Filter einen Pixel weiter nach rechts bewegt, sind alle Pixel unter dem Filter weiß, das Pixel bleibt somit weiß.

Damit ist es möglich, dicke Linien dünner zu machen, sowie dünne Linien zu entfernen.

\newpage

### Entfernen von Spulen

Wird nun das binäre Bild invertiert und diese Funktion mit einer Filtergröße von der dreifachen zuvor ausgerechneten Liniendicke angewandt, bleibt nur noch die Spule zurück. 

![Entfernen der Schaltung bis auf Spulen](.\Dateien\Erode.png){width=100%}

Danach wird die Differenz zwischen dem invertiertem Binärbild und dem "Erosion" Bild gebildet. Dadurch wird die Fläche in der Spule entfernt. Zuletzt wird das Bild erneut invertiert, um wieder auf das ursprüngliche Format zurückzukommen.

![Differenz zwischen den beiden Bildern](.\Dateien\spuleWeg.png){width=100%}

\newpage

### Umwandeln des Bildes

Um alle Linien in eine Breite von einem Pixel umzuwandeln, wird die Funktion "ximgproc.thinning" aus der Library OpenCV verwendet. Diese liefert als Rückgabewert das konvertierte Bild.

![Bild mit einer Linienbreite von einem Pixel](.\Dateien\thinn.png){width=75%}