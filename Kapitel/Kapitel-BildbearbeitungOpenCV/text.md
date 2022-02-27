# Bildbearbeitung mit OpenCV

## Problem

Um das Bild der Schaltung weiter verarbeiten zu können, ist es wichtig, alle Linien in dem Bild der Schaltung auf eine breite von einem Pixel zu ändern.

## Idee

Mithilfe einer Funktion aus der Paython Library OpenCV soll jede Linien in dem Bild in eine Linie mit einer breite von einem Pixel umgewandeldt werden.

![Binary](.\Dateien\binary.png) ![Thinn](.\Dateien\thinn.png)

### Problem bei Spulen

Diese Algorithmus funktiuoniert jedoch bei Spulen nicht, da diese für den Algorithmus nur eine breitere Linie wie die Verbindungen zwischen den Bauteilen darstellen und somit auch zu einer ein Pixel breiten Linie geändert werden.

![Binary](.\Dateien\binary.png) ![Thinn ohne Spulen](.\Dateien\thinnOhneSpule.png)

### Lösung für Spulen

Um zu verhindern dass Spulen entfernt werden, werden zuerst die schwarzen Flächen in den Spulen entfernt. Spulen haben somit die gleiche Struktur wie Widerstände und können in eine ein Pixel breite Linie umgewandelt werden.

![Binary](.\Dateien\binary.png) ![ohne Spulen](.\Dateien\ohneSpulen.png)


## Umsetzung

### Entfernen von Spulen

Zuerst wir eine Liste erstellt, zu der die Koordinaten von allen schwarzen Pixel im Bild hinzugefügt werden.

Danach wird Filter erstellt, welcher ein zweidimensionaler Array ist, der nur aus schwarzen Pixel besteht. 

Bei allen zuvor in der Liste gespeicherten Koordinaten wird nun im Bild der Schaltung überprüft, ob das Bild an diesen Koordinaten dem Filter gleicht. Sind die beiden identisch werden die Koordinaten in einer weiteren Liste abgespeichert.

Zuletzt werden im Bild alle Pixel aus der zweiten Liste mit weißen Pixel ersetzt.

### Umwandeln des Bildes

Um alle Linien in eine breite von einem Pixel umzuwandeln wird die Funktion "thinnImage()" aus der Library OpenCV aufgerufen. Diese liefert als rückgabewert das konvertierte Bild.
