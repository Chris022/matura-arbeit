# Bildbearbeitung mit OpenCV

## Problem

Um das Bild der Schaltung weiter verarbeiten zu können, ist es wichtig, alle Linien in dem Bild der Schaltung auf eine breite von einem Pixel zu ändern.

## Idee

Mithilfe einer Funktion aus der Paython Library OpenCV soll jede Linien in dem Bild in eine Linie mit einer breite von einem Pixel umgewandeldt werden.

|||
:-:|:-:
![Binary](.\Dateien\binary.png){width=40%} | ![Thinn](.\Dateien\thinn.png){width=40%}

### Problem bei Spulen

Diese Algorithmus funktiuoniert jedoch bei Spulen nicht, da diese für den Algorithmus nur eine breitere Linie wie die Verbindungen zwischen den Bauteilen darstellen und somit auch zu einer ein Pixel breiten Linie geändert werden.

|||
:-:|:-:
![Binary](.\Dateien\binary.png){width=40%} | ![Thinn ohne Spulen](.\Dateien\thinnOhneSpule.png){width=40%}

### Lösung für Spulen

Um zu verhindern dass Spulen entfernt werden, werden zuerst die schwarzen Flächen in den Spulen entfernt. Spulen haben somit die gleiche Struktur wie Widerstände und können in eine ein Pixel breite Linie umgewandelt werden.

||||
:-:|:-:|:-:
![Binary](.\Dateien\binary.png){width=35%} | ![ohne Spulen](.\Dateien\ohneSpulen.png){width=35%} | ![Thinn](.\Dateien\thinn.png){width=35%}


## Umsetzung

### Durchschnittliche Dicke einer Linie

Um Spulen entfernen zu können, muss zuerst die Dicke der Linien in der Schaltung herausgefunden werden.

Dafür wird in jeder Spalte jeder Pixel nacheinander überprüft. Sobald ein Pixel schwarz ist, hat man eine Linie gefunde. Ein Zähler wird ab diesem Pixel so lange erhöht bis wieder ein weißer Pixel auftritt und die gezeichnete Linie somit endet. Nach jeder Linie wird die Dicke der Linie in dieser Spalte in eine Liste gespeichert. 

Beispiel einer Linie welche in der rot makierten Spalte drei Pixel breit ist.

![Linien Dicke in einer Spalte](.\Dateien\lineThick.png){width=40%}

Als durchschnittliche Liniendicke wird der Wert gewählt, welcher bbei den in der Liste gespeicherten Breiten am häufigsten auftritt.


### Entfernen von Spulen

Um Spulen zu entfernen wird die Funktion "erode" aus der Library OpenCV verwendet. Dabei wird eine Filtermaske über ein Bild geschoben. Ein Pixel im original Bild bleibt nur dann weiß, wenn alle Pixler unter dem Filter weiß sind.

![Funktion "erode" Beispiel 1](.\Dateien\erode1.png){width=60%}

Unter dem 3x3 Filter sind schwarze und weiße Pixel somit wird der Pixel im Zentrum des Filters schwarz.

![Funktion "erode" Beispiel 2](.\Dateien\erode2.png){width=60%}

Wird der Filter einen Pixel weiter nach rechts bewegt, sind alle Pixel unter dem Filter weiß, der Pixel bleibt somit weiß.

Damit ist es möglich dicke Linien dünner zu machen, sowie dünne Linien zu entfernen.

Wird nun das Binäre Bild invertiert, und diese Funktion mit einer Filtergröße von derr dreifachen zuvor ausgerechneten Liniendicke angewandt, bleibt nur noch die Spule zurück. 

|||
:-:|:-:
![Invertiertes Binärbild](.\Dateien\InvBinary.png){width=40%} | ![Bild nach Funktion "erode"](.\Dateien\erosion.png){width=40%}

Danach wird die Differenz zwischen dem Invertiertend Binärbild und dem "Erosion" Bild gebildet. Dadurch wird die Fläche in der Spule entfernt. Zuletzt wird das Bild wieder invertiert, um wieder auf das uzrsprüngliche Format zurückzukommen.

|||
:-:|:-:
![Differenz zwischen den beiden Bildern](.\Dateien\InvOhneSpulen.png){width=40%} | ![ohne Spulen](.\Dateien\ohneSpulen.png){width=40%}


### Umwandeln des Bildes

Um alle Linien in eine breite von einem Pixel umzuwandeln wird die Funktion "thinnImage()" aus der Library OpenCV aufgerufen. Diese liefert als rückgabewert das konvertierte Bild.

![Thinn](.\Dateien\thinn.png){width=50%}