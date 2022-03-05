# Umwandeln der Schaltung in eine Graph Datenstruktur

## Begriffe

### Richtungs-Gradient
Ist ein Konstrukt, welches eine Liste von besuchten Koordinaten mitführt. Bei jeder neu hinzugefügten Koordinate wird die Richtung der letzten N Koordinaten geprüft. Sollte diese Richtung durchschnittlich eine andere sein als jene zu vor wir eine Richtungsänderung erkannt!

![Beschreibung eines Richtungs-Gradienten](.\Dateien\RichtungsGradient.png) 

## Problem
Für eine leichtere Verarbeitung/Bearbeitung sollte das Bild der Schaltung in eine Datenstruktur umgewandelt werden. Da ein Graph die in dem Bild der Schaltung enthaltene Information sehr gut speichert, wurde diese Datenstruktur gewählt. Für eine genauere Beschreibung siehe Kapitel zuvor.

## Idee
Mithilfe eines rekursiven Algorithmus sollen die schwarzen Pixel in der Schaltung, Pixel für Pixel verfolgt werden.

So sollen alle Eckpunkte, Endpunkte und Verzweigungen gefunden werden, in je einen Vertex umgewandelt und sinnvoll zu einem Graphen zusammengefügt werden. Jeder der drei Fälle soll dabei ein Vertex mit je einer anderen Farbe sein.

![Unterschiedliche Typen von Vertices](.\Dateien\SchaltungBild1.png){width=50%}


## Umsetzung

![Blockschaltbild des rekursiven teils des Algorithmus](.\Dateien\AlgorithmusBlockschaltbild.png){width=70%}

![Beispiel Szenario](.\Dateien\AlgorithmusBild1.png){width=60%}

![Der von oben generierte Graph bei den einzelnen Zwischenschritten](.\Dateien\AlgorithmusBild2.png){width=60%}

## Algorithmus

Der Graph wird nach folgendem Algorithmus generiert.

Als Input für den Algorithmus muss ein, laut vorherigen Kapitelen bearbeites Bild, als 2D-Array übergeben werden.
Richtungsänderungen werden mithilfe eines Richtungs-Gradienten erkannt. Für eine Erklärung siehe Richtungs-Gradient zuvor.

```
erstelle ein leeres Graph Objekt
while - es existieren noch schwarze Pixel im Bild
	finde die Koordinaten eines zufälligen, schwarzen Pixels
	führe "generatePartGraph" mit gefunden Koordinaten aus
	führe den generierten Graphen mit dem zuvor erstellen zusammen
	färbe alle besuchten Pixel weiß
```

```
subroutine "generatePartGraph"(startPoint):

	finde alle schwarzen, benachbarten Pixel des gegebenen Startpunktes

	je nach Anzahl der gefunden Pixel
	 	1 Nachbar:Endpunkt
			füge einen Vertex mit der blauen Farbe hinzu
	 	2 Nachbarn:Ein normales Verbindungsstück
		 	füge einen Vertex mit der pinken Farbe hinzu
	 	mehr als 2 Nachbarn:Eine Verzweigung
			füge einen Vertex mit der pinken Farbe hinzu

	rufe die Subroutine "rekursiv" auf mit:
		currentPixel = startPunkt
		lastPixel = [0,0]
		lastGraphNode = zuvor erzeugter Vertex
		directionGradient = neuer Richtungs Gradient

	return erstellen Graph und besuchte Pixel

```

```
subroutine "rekursiv"(currentPixel,lastPixel,lastGraphNode,directionGradient)
	füge eines neuen Schritt zum Richtungs-Gradient hinzu

	prüfe ob der gereade besuchte Pixel bereits zuvor besucht wurde
		wenn ja ->
			verbinde den Verbindungs-Vertex mit dem letzt erstellten Vertex
			return

	markiere den gerade besuchten Pixel als besucht

	hole alle zum gerade besuchten Pixel, benachbarten Pixel
		jedoch nicht den zuvor besuchten Pixel

	je nach Anzahl der Nachbarn:
		0 Nachbarn: Endpunkt
			füge einen Endpunkt-Vertex zum Graphen hinzu
			verbinde diesen mit dem zuletzt erstellen Vertex

		1 Nachbar: einfache Verbindungslinie
			prüfe ob der Richtungs-Gradient eine Ecke findet
				wenn ja ->
					füge einen Eckpunkt-Vertex  zum Graphen hinzu
					verbinde diesen mit dem zuletzt erstellen Vertex
					rufe die Subroutine "rekursiv" auf mit:
						currentPixel = Nachbar-Pixel
						lastPixel = gerade besuchter Pixel
						lastGraphNode = gerade erstellter Vertex
						directionGradient = neuer Richtungs-Gradient
				wenn nein -> 
	            	rufe die Subroutine "rekursiv" auf mit:
						currentPixel = Nachbar-Pixel
						lastPixel = gerade besuchter Pixel
						lastGraphNode = zuletzt erstellter Vertex
						directionGradient = Richtungs-Gradient
		mehr als 1 Nachbar:
			füge dem Graphen einen Verzweigungs-Vertex und
			verbinde diesen mit dem zuletzt erstellen Vertex
	
	        für jeden Nachbar:
	        	rufe die Subroutine "rekursiv" auf mit:
					currentPixel = Nachbar-Pixel
					lastPixel = gerade besuchter Pixel
					lastGraphNode = gerade erstellter Vertex
					directionGradient = Richtungs-Gradient
```