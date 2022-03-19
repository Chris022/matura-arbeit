# Umstrukturieren des Graphen

## Problem
Um den Graphen nun besser in ein von Simulatoren verständliches File umzuwandeln, muss er zuvor noch umstrukturiert werden. Als Erstes müssen alle Koordinaten in relative Werte umgewandelt werden. Dies ist nötig, da die Bauteile im Simulatorenprogramm eine fixe Größe haben. Ist nun allerdings eine Schaltung sehr klein gezeichnet, wäre eine Umwandlung nicht möglich!

![Eine solche Umwandlung wäre nicht möglich, da bereits der Widerstand größer ist als die gesamte Schaltung](.\Dateien\ProblemMitUmwandlung.png){width=60%}

Auch müssen alle Bauteile noch neu positioniert werden, um geradlinige Linienführung garantieren zu können.

![Problem mit nicht geradlinigen Linienführungen](.\Dateien\FromTo.png){width=60%}

## Idee
Mithilfe eines Algorithmus soll der Graph so umstrukturiert werden, dass alle Bauteile zu je einem Vertex zusammengefasst werden.

![Umstrukturierung des Graphen](.\Dateien\Umstruckturieren1.png){width=60%}

Die Umwandlung in relativen Koordinaten soll geschehen, indem zuerst die durchschnittliche Länge der gezeichneten Widerstände ermittelt wird. Dann sollen alle Koordinaten so skaliert werden, dass die gezeichneten Widerstände genau so groß sind wie die Widerstände im Simulatorenprogramm.

![Skalieren der Koordinaten](.\Dateien\ProblemMitUmwandlungLösung.png){width=60%}

Mithilfe eines weiteren rekursiven Algorithmus, welcher Bauteil für Bauteil alle Bauteile besucht, sollen jene dann, wie in dem "Problem" bereits geschrieben, gerade gerichtet werden.

## Umsetzung
### Konvertierung zu relativen Koordinaten
Zuerst werden die Bauteilinformationen wie Rotation, Art des Bauteils und Bauteil-Vertices genutzt, um die durchschnittliche Länge der gezeichneten Widerstände zu ermitteln. Dann werden alle Koordinaten, sowohl X als auch Y durch diese Länge dividiert und mit der Länge des Widerstandes im Simulatoren-Programm multipliziert.

### Umstrukturieren des Graphen
Für jedes vom vorherigen Schritt gefundenes Bauteil wird ein neuer, grüner Vertex in den Graphen eingefügt.

![Einfügen eines grünen Vertex für jedes Bauteil](.\Dateien\Umstruckturieren2.png){width=50%}

Anschließend werden die eigentlichen Vertices des Bauteils entfernt. Dies alles geschieht mithilfe der "group" Methode, welche unsere Graph-Bibliothek für ein Graph Objekt zur Verfügung stellt.

![Entfernen der übrigen Bauteil-Vertices](.\Dateien\Umstruckturieren3.png){width=50%}

Dann werden für die Verbindungen zwischen den Bauteilen noch neue Verbindungs-Vertices eingefügt.

![Einfügen von Verbindungs-Vertices](.\Dateien\Umstruckturierung4.png){width=50%}

Die Bauteile werden dann als extra Vertices aus dem Graphen genommen.

![Bauteile ausgliedern](.\Dateien\Umstruckturierung5.png){width=50%}

### Bauteile gerade richten
Beginne bei einem beliebigen Vertex. Besuche dessen Nachbarn. Vergleiche die Koordinaten der Nachbarn mit den Koordinaten des gerade besuchten Vertex.
$$
    dX = X1 - X2
$$
$$
    dY = Y1 - Y2
$$

ist $dX$ größer, so setzte die Y Koordinate des Nachbars = der Y Koordinate des gerade besuchten Vertex  
bei $dY$ größer, setzte die X Koordinate des Nachbars = der X Koordinate des gerade besuchten Vertex

![dY ist kleiner und wird somit zu 0 gemacht](.\Dateien\GeradeRichten.png){width=40%}

Wiederhole dies für alle Nachbarn bis alle Vertices einmal besucht wurden

### Beschreibung des Algorithmus  

```
finde einen Eck-Vertex als Startpunkt

subroutine "traversial"(currentVertex,lastVertex)
    berechne X1-X2 von dem gerade besuchten und zuletzt besuchten Vertex
    berechne Y1-Y2 von dem gerade besuchten und zuletzt besuchten Vertex
    wenn X1-X2 kleiner
        setze X Position vom gerade besuchten Vertex
        zur X Position des zuletzt besuchten Vertex
    sonst
        setze Y Position vom gerade besuchten Vertex
        zur Y Position des zuletzt besuchten Vertex

    hole alle Nachbarn des gerade besuchten Vertex
    für jeden Nachbar
        wenn Nachbar nicht gleich zuletzt besuchter Vertex
            rufe Subroutine "traversial" auf mit:
                currentVertex = Nachbar
                lastVertex = currentVertex
```
\newpage

### Bauteile gerade richten (nicht genutzt)
Die Idee war es einfach alle Koordinaten auf einen gewissen Wert zu runden, so würde [175,142] zu [180,140] werden.  
**Problem**: Schaltungen werden unterschiedlich groß gezeichnet. Somit müssten die Koordinaten auch auf unterschiedliche Werte gerundet werden. Dies ist allerdings kaum machbar.