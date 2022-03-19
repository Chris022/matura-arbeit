# Finden der Bauteile

## Problem
Damit später die Bauteile in ein Simulationsprogramm eingefügt werden können, muss als erstes die Position der Bauteile innerhalb der Schaltung gefunden werden.

## Idee
In dem Graph sucht man nach bestimmten Mustern, welche ein Bauteil darstellen. Dadurch dass in jedem Vertex die original Koordinaten gespeichert sind, kann dann die Positon des jeweiligen Bauteils im Ausgangsbild gefunden werden.

## Umsetzung

Im Graphen, ist jedes Bauteil relativ leicht anhand seines Musters zu idendifizieren.

![Muster für ein Gnd Symbol im Graphen](.\Dateien\MusterGnd.png)

![Muster für einen Widerstand im Graphen](.\Dateien\MusterWiderstand.png)

Mithilfe der Muster-Findungs-Funktion die unsere Graph Bibliothek zur Verfügung stellt, können die Muster dann sehr leicht gefunden werden. Da in jedem Vertex dann noch seine Koordinaten im Bild gespeichert sind, können dann sehr leicht sogenannte Bounding Boxes erstellt werden.Wichtig ist, dass in diesem Schritt lediglich die Position der Bauteile gefunden, nicht die Art des Bauteils.

![Beispielschaltung mit eingezeichneten Boundingboxen](.\Dateien\boundingboxes.png){width=50%}

**Wichtig:**Um manche Bauteile (besonders Kondensatoren) zu erkennen, muss der Graph, bevor Muster gefunden werden können, noch modifiziert werden. Ein Kondensator würde ohne diese Modifikation wie 2 Ground Symbole aussehen.

![Muster eines Ground Symbols(links) und eines Kondensators(rechts)](.\Dateien\KondensatorGndMuster.png){width=50%}

Im Falle eines Kondensators wird geprüft, ob zwei Ground Symbole direkt gegenüber voneinander stehen. Sollte dies der Fall sein, wird der Graph so verändert, dass ein Kondensator eindeutig identifizierbar ist.

![Die Veränderung des Kondensator Musters](.\Dateien\VeraenderungKondensator.png){width=50%}