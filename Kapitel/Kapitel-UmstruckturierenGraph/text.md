# Umstrukturieren des Graphen

## Problem
Um den Graphen besser in ein von Simulatoren verständliches File umzuwandeln, muss er zuvor noch umstrukturiert werden. Als Erstes müssen alle Koordinaten vergrößert oder verkleinert werden, sodass ein gezeichnetes Bauteil gleich groß ist als ein Bauteil im Simulator. Dies ist nötig, da die Bauteile im Simulatorenprogramm eine fixe Größe haben. Ist nun allerdings eine Schaltung sehr klein gezeichnet, wäre eine Umwandlung nicht möglich!

![Eine solche Umwandlung wäre nicht möglich, da bereits der Widerstand im Simulator (rechts) größer ist als die gesamte gezeichnete Schaltung(links)](.\Dateien\ProblemMitUmwandlung.png){width=60%}

Auch müssen alle Bauteile neu positioniert werden, um eine geradlinige Linienführung garantieren zu können.

![Nicht geradlinige Linienführung](.\Dateien\FromTo.png){width=60%}

## Idee
Mithilfe eines Algorithmus soll der Graph so umstrukturiert werden, dass alle Bauteile zu je einem Vertex zusammengefasst werden.

![Umstrukturierung des Graphen](.\Dateien\Umstruckturieren1.png){width=60%}

Die Vergrößerung oder Verkleinerung der Koordinaten soll geschehen, indem zuerst die durchschnittliche Länge der gezeichneten Widerstände ermittelt wird. Dann sollen alle Koordinaten so skaliert werden, dass die gezeichneten Widerstände genau so groß sind wie die Widerstände im Simulatorenprogramm.

![Skalieren der Koordinaten](.\Dateien\ProblemMitUmwandlungLösung.png){width=60%}


Mithilfe eines rekursiven Algorithmus, welcher nacheinander alle Bauteile besucht, sollen jene dann noch, wie bereits geschrieben, gerade gerichtet werden.

## Umsetzung
### Konvertierung der Koordinaten
Zuerst werden die Bauteilinformationen wie Rotation, Art des Bauteils und Bauteil-Vertices genutzt, um die durchschnittliche Länge der gezeichneten Widerstände zu ermitteln. Dann werden alle Koordinaten, sowohl X als auch Y durch diese Länge dividiert und mit der Länge des Widerstandes im Simulatoren-Programm (=80) multipliziert.

### Umstrukturieren des Graphen
Für jedes vom vorherigen Schritt gefundenes Bauteil wird ein neuer, grüner Vertex in den Graphen eingefügt.

![Einfügen eines grünen Vertex für jedes Bauteil](.\Dateien\Umstruckturieren2.png){width=50%}

Anschließend werden die eigentlichen Vertices des Bauteils entfernt. Dies alles geschieht mithilfe der "group" Methode, welche die Graph-Bibliothek für ein Graph Objekt zur Verfügung stellt.

![Entfernen der übrigen Bauteil-Vertices](.\Dateien\Umstruckturieren3.png){width=50%}

Dann werden für die Verbindungen zwischen den Bauteilen noch neue Verbindungs-Vertices eingefügt.

![Einfügen von Verbindungs-Vertices](.\Dateien\Umstruckturierung4.png){width=50%}


### Bauteile gerade richten
Zum Geraderichten der Bauteile wird bei einem belibigen Vertex begonnen und dessen Nachbarn besucht. Anschließend werden die Koordinaten der Nachbarn mit den Koordinaten des gerade besuchten Vertex verglichen.
$$
    dX = X1 - X2
$$
$$
    dY = Y1 - Y2
$$

Ist hierbei $dX$ größer, wird die Y Koordinate des Nachbars gleich der Y Koordinate des gerade besuchten Vertex gesetzt.
Ist hingengen $dY$ größer wird die X Koordinate des Nachbars gleich der X Koordinate des gerade besuchten Vertex gesetzt.

![dY ist kleiner und wird somit zu 0 gemacht](.\Dateien\GeradeRichten.png){width=40%}

Wiederhole dies für alle Nachbarn, bis alle Vertices einmal besucht wurden.

\newpage