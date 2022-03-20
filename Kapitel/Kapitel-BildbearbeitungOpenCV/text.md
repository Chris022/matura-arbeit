# Bildbearbeitung mit OpenCV

## Problem

Um das Bild der Schaltung weiter verarbeiten zu können, ist es wichtig, alle Linien in dem Bild der Schaltung auf eine breite von einem Pixel zu verändern.

## Idee

Mithilfe einer Funktion aus der Python Library OpenCV soll jede Linien in dem Bild in eine Linie mit einer breite von einem Pixel umgewandeldt werden.

![Binärbild und gewünschtes Ergebnis](.\Dateien\Ziel.png){width=100%}

### Problem bei Spulen

Diese Algorithmus funktiuoniert jedoch bei Spulen nicht, da diese für den Algorithmus nur eine breitere Linie wie die Verbindungen zwischen den Bauteilen darstellen und somit auch zu einer ein Pixel breiten Linie geändert werden.

![Problem bei Spulen](.\Dateien\problemSpulen.png){width=100%}

### Lösung für Spulen

Um zu verhindern dass Spulen entfernt werden, werden zuerst die schwarzen Flächen in den Spulen entfernt. Spulen haben somit die gleiche Struktur wie Widerstände und können in eine ein Pixel breite Linie umgewandelt werden.

![Lösung für Spulen](.\Dateien\lösungSpulen.png){width=100%}

## Umsetzung

### Durchschnittliche Dicke einer Linie

Um Spulen entfernen zu können, muss zuerst die durchschnittliche Dicke der Linien in der Schaltung herausgefunden werden.

Dafür wird in jeder Spalte jeder Pixel nacheinander überprüft. Sobald ein Pixel schwarz ist, hat man eine Linie gefunde. Ein Zähler wird ab diesem Pixel so lange erhöht bis wieder ein weißer Pixel auftritt und die gezeichnete Linie somit endet. Nach jeder Linie wird die Dicke der Linie in dieser Spalte in eine Liste gespeichert. 

Beispiel einer Linie welche in der rot makierten Spalte drei Pixel breit ist.

![Linien Dicke in einer Spalte](.\Dateien\lineThick.png){width=40%}

Als durchschnittliche Liniendicke wird der Wert gewählt, welcher bei den in der Liste gespeicherten Breiten am häufigsten auftritt.


### Entfernen von Spulen

Um Spulen zu entfernen wird die Funktion "erode" aus der Library OpenCV verwendet. Dabei wird eine Filtermaske über ein Bild geschoben. Ein Pixel im original Bild bleibt nur dann weiß, wenn alle Pixler unter dem Filter weiß sind.

![Funktion "erode" Beispiel 1](.\Dateien\erode1.png){width=60%}

Unter dem 3x3 Filter sind schwarze und weiße Pixel somit wird der Pixel im Zentrum des Filters schwarz.

![Funktion "erode" Beispiel 2](.\Dateien\erode2.png){width=60%}

Wird der Filter einen Pixel weiter nach rechts bewegt, sind alle Pixel unter dem Filter weiß, der Pixel bleibt somit weiß.

Damit ist es möglich dicke Linien dünner zu machen, sowie dünne Linien zu entfernen.

Wird nun das Binäre Bild invertiert, und diese Funktion mit einer Filtergröße von der dreifachen zuvor ausgerechneten Liniendicke angewandt, bleibt nur noch die Spule zurück. 

![Entfernen der Schaltung bis auf Spulen](.\Dateien\Erode.png){width=100%}

Danach wird die Differenz zwischen dem Invertiertend Binärbild und dem "Erosion" Bild gebildet. Dadurch wird die Fläche in der Spule entfernt. Zuletzt wird das Bild wieder invertiert, um wieder auf das uzrsprüngliche Format zurückzukommen.

![Differenz zwischen den beiden Bildern](.\Dateien\spuleWeg.png){width=100%}


### Umwandeln des Bildes

Um alle Linien in eine breite von einem Pixel umzuwandeln wird die Funktion "thinnImage" aus der Library OpenCV verwendet. Diese liefert als rückgabewert das konvertierte Bild.

![Bild mit einer Linienbreite von einem Pixel](.\Dateien\thinn.png){width=80%}