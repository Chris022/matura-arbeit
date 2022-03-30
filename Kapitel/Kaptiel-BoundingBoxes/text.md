# Finden der Bauteile

## Problem
Damit später die Bauteile in ein Simulationsprogramm eingefügt werden können, muss als erstes die Position der Bauteile innerhalb der Schaltung gefunden werden.

## Idee
In dem Graph soll nach bestimmten Mustern, welche ein Bauteil darstellen, gesucht werden. Dadurch dass man von jedem Knotenpunkt weiß, wo, im original Bild dieser Liegt, kann so dann die Positon des jeweiligen Bauteils gefunden werden.

## Umsetzung

Im Graphen ist jedes Bauteil relativ leicht anhand seines Musters zu idendifizieren.

![Muster für ein Ground Symbol im Graphen](.\Dateien\MusterGnd.png)

![Muster für einen Widerstand im Graphen](.\Dateien\MusterWiderstand.png)

Mithilfe der Muster-Findungs-Funktion, die die Graph Bibliothek zur Verfügung stellt, können die Muster dann sehr leicht gefunden werden. Da in jedem Vertex seine Koordinaten im Bild gespeichert sind, können sehr leicht sogenannte Bounding Boxes erstellt werden.
Wichtig ist, dass in diesem Schritt lediglich die Position der Bauteile gefunden wird, nicht die Art des Bauteils. Der Grund dafür wird im nächsten Kapitel noch beschrieben.

![Beispielschaltung mit eingezeichneten Boundingboxen](.\Dateien\boundingboxes.png){width=50%}

**Wichtig:** Um manche Bauteile (besonders Kondensatoren) zu erkennen, muss der Graph, bevor Muster gefunden werden können, noch modifiziert werden. Ein Kondensator würde ohne diese Modifikation wie zwei Ground Symbole aussehen.

![Muster eines Ground Symbols (links) und eines Kondensators (rechts)](.\Dateien\KondensatorGndMuster.png){width=50%}

Im Falle eines Kondensators wird geprüft, ob zwei Ground Symbole direkt gegenüber voneinander stehen. Sollte dies der Fall sein, wird der Graph so verändert, dass ein Kondensator eindeutig identifizierbar ist.

![Die Veränderung eines Beispiel Graphen zur Erkennung eines Kondensators](.\Dateien\VeraenderungKondensator.png){width=50%}