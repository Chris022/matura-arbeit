# Umwandeln der Schaltung in eine Graph Datenstruktur

## Begriffe
### Graph
Ein Graph ist eine Sonderform einer Baum-Datenstruktur.

![Beispiel für einen Graphen](.\Dateien\GraphBild1.png)

Sie besteht aus sogenannten "Vertices" und "Edges".

![Bestandsteile eines Graphen](.\Dateien\GraphBild2.png)

Wobei je ein Vertex einen Datenpunkt repräsentiert,welcher mithilfe einer Edge mit anderen Datenpunkten verbunden ist. Jeder Vertex und jede Edge kann auch noch eine bestimmte Farbe haben. So kann zwischen zwei Strukturen, die zwar strukturell gleich sind, aber je andere Dinge darstellen unterschieden werden.

![Strukturell gleiche Graphen, welche sich lediglich durch die Farbe unterscheiden](.\Dateien\GraphBild3.png) 

In jedem Vertex können hierbei auch unterschiedliche Daten, wie zum Beispiel: Koordinaten gespeichert werden, diese unterscheiden zwei Graphen allerdings **nicht** von einander!

### Richtungs-Gradient
Ist ein Konstrukt welches eine Liste von besuchten Koordinaten mitführt. Bei jeder neu hinzugefügten Koordinate wird die Richtung der letzten N Koordinaten geprüft. Sollte diese Richtung durchschnittlich eine andere sein als jene zu vor, wir eine Richtungsänderung erkannt!

![Beschreibung eines Richtungs-Gradienten](.\Dateien\RichtungsGradient.png) 

### Problem
Für eine Leichtere Verarbeitung/Bearbeitung sollte das Bild der Schaltung in eine Datenstruktur umgewandelt werden. Da ein sogenannter Graph die in dem Bild der Schaltung enthaltene Information sehr gut speichert wurde diese Datenstruktur gewählt.

### Idee
Mithilfe eines rekursiven Algorithmus sollen die schwarzen Pixel in der Schaltung, Pixel für Pixel verfolgt werden.

![Unterschiedliche Typen von Vertices](.\Dateien\SchaltungBild1.png){width=50%}

So sollen alle Eckpunkte, Endpunkte und Verzweigungen gefunden werden, in je einen Vertex umgewandelt und sinnvoll zu einem Graphen zusammengefügt werden. Jeder der drei Fälle soll dabei ein Vertex mit je einer anderen Farbe sein.

### Umsetzung

### Beschreibung der Grundstruktur des Algorithmus

![Blockschaltbild des rekursiven teils des Algorithmus](.\Dateien\AlgorithmusBlockschaltbild.png){width=70%}

![Beispiel Szenario](.\Dateien\AlgorithmusBild1.png){width=60%}

![Der von oben generierte Graph bei den einzelnen Zwischenschritten](.\Dateien\AlgorithmusBild2.png){width=60%}

### Algorithmus in Text Form

Der Graph wird nach folgendem Algorithmus generiert.

Als Input für den Algorithmus muss ein, laut vorheriger Kapitel bearbeites Bild, als 2D-Array übergeben werden.
Richtungsänderungen werden mithilfe eines Richtungs-Gradienten erkannt. Für eine Erklärung siehe Richtungs-Gradient zuvor.

```
erstelle ein leeres Graph Objekt <empty Graph>
while - es existieren noch schwarze Pixel im Bild
	finde die Koordinaten eines zufälligen, schwarzen Pixels
	führe "generatePartGraph" mit gefunden Koordinaten aus
	führe den generierten Graphen mit <empty Graph> zusammen
	färbe alle besuchten Pixel weiß
```

```
subroutine generatePartGraph(startPoint):

Erstelle einen leeren Graphen <graph>
Erstelle einen leeren Array in dem alle besuchten Pixel
gespeichert werden <visitedPixels>

Finde alle schwarzen, benachbarten Pixel des gegebenen Startpunktes
je nach Anzahl der gefunden Pixel handelt es sich bei dem start Punkt um einen
 1 Nachbar = Endpunkt (Farbe: blau)
 2 Nachbarn = Ein normales Verbindungsstück (Farbe: pink)
 mehr als 2 Nachbarn = Eine Verzweigung (Farbe: rot)

Füge einen Vertex mit der passenden Farbe und den Koordinaten des
Startpunktes zum Graphen hinzu

führe die rekursieve subroutine mit:
	currentPixel = startPunkt
	lastPixel = [0,0]
	lastGraphNode = zuvor erzeugter Vertex
	directionGradient = neuer Richtungs Gradient

return <graph> und <visitedPixels>

```

```
rekursieve subroutine(currentPixel,lastPixel,lastGraphNode,directionGradient)
füge eines neuen Schritt zum Richtungs-Gradient hinzu

prüfe ob der gereade besuchte Pixel bereits zuvor besucht wurde (ist <currentPixel> in <visitedPixels>)
	wenn ja -> verbinde den Verbindungs-Vertex mit der <lasGraphNode>
		return
füge den <currentPixel> zu <visitedPixel> hinzu
hole alle zu <currentPixel> benachbarten Pixel ohne <lastPixel>

je nach Anzahl der Nachbarn:
	0 Nachbarn: Endpunkt
		füge einen Endpunkt-Vertex mit den Koordinaten in <currentPixel> zum Graphen hinzu und verbinde diesen mit <lastGraphNode>
	
	1 Nachbar: einfache Verbindungslinie
		Prüfe ob der Richtungs-Gradient eine Ecke findet
			wenn ja -> füge einen Eckpunkt-Vertex mit den Koordinaten in <currentPixel> zum Graphen hinzu und verbinde diesen mit <lastGraphNode> 
			rufe die Subroutine recursiv auf mit:
				currentPixel = nachbarPixelKoordinaten
				lastPixel = <currentPixel>
				lastGraphNode = gerade erstellter Vertex
				directionGradient = neuer Richtungs-Gradient
			wenn nein -> 
            	rufe die Subroutine recursiv auf mit:
					currentPixel = nachbarPixelKoordinaten
					lastPixel = <currentPixel>
					lastGraphNode = <lastGraphNode>
					directionGradient = <direction Gradient>
	mehr als 1 Nachbar:
		Füge dem Graphen einen Verzweigungs-Vertex mit den koordinaten <currentPixel> hinzu und
		verbinde diesen mit <lastGraphNode>
        
        für jeden Nachbar:
        	rufe die Subroutine recursiv auf mit:
					currentPixel = nachbarPixelKoordinaten
					lastPixel = <currentPixel>
					lastGraphNode = gerade erstellter Vertex
					directionGradient = <direction Gradient>
```