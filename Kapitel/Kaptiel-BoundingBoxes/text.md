# Finden der Bauteile

## Problem
Damit später die Bauteile in ein Simulationsprogramm eingefügt werden können, muss als erstes die Position der Bauteile innerhalb der Schaltung gefunden werden.

## Idee
In dem Graph soll nach bestimmten Mustern, welche ein Bauteil darstellen, gesucht werden. Dadurch, dass man von jedem Knotenpunkt weiß, wo im Originalbild dieser liegt, kann so dann die Position des jeweiligen Bauteils gefunden werden.

## Umsetzung

Im Graphen ist jedes Bauteil relativ leicht anhand seines Musters zu idendifizieren.

![Muster für ein Ground Symbol im Graphen](.\Dateien\MusterGnd.png)

![Muster für einen Widerstand im Graphen](.\Dateien\MusterWiderstand.png)

Mithilfe der Muster-Findungs-Funktion, die die Graph Bibliothek zur Verfügung stellt, können diese Muster sehr leicht gefunden werden. Da in jedem Vertex seine Koordinaten im Bild gespeichert sind, können sogenannte Bounding Boxes erstellt werden.
Wichtig ist, dass in diesem Schritt lediglich die Position der Bauteile gefunden wird, nicht die Art des Bauteils. Der Grund dafür wird im nächsten Kapitel noch erläutert.

![Beispielschaltung mit eingezeichneten Boundingboxen](.\Dateien\boundingboxes.png){width=50%}

**Wichtig:** Um manche Bauteile (besonders Kondensatoren) zu erkennen, muss der Graph, bevor ein Muster gefunden werden kann, noch modifiziert werden. Ohne diese Modifikation könnte ein Kondensator nicht von zwei Ground Symbolen unterschieden werden.

![Muster eines Ground Symbols (links) und eines Kondensators (rechts)](.\Dateien\KondensatorGndMuster.png){width=50%}

Im Falle eines Kondensators wird geprüft, ob zwei Ground Symbole direkt gegenüber voneinander stehen. Sollte dies der Fall sein, wird der Graph so verändert, dass ein Kondensator eindeutig identifizierbar ist.

![Die Veränderung eines Beispiel Graphen zur Erkennung eines Kondensators - Version 1](.\Dateien\VeraenderungKondensator-1.png){width=50%}

Würden die Ground Symbole jedoch lediglich verbunden werden, ergäbe sich ein weiteres Problem. Sind zwei Kondensatoren direkt nebeneinander palziert, würden drei anstelle von den gewollten zwei Kondensatoren gefunden werden.

![Problem beim plazieren von zwei Kondensatoren nacheinander - Problem](.\Dateien\ProblemMit2Kond-1.png){width=50%}

Behoben wird dies, indem die zwei Ground Muster nicht durch eine schwarze Edge, sondern duch eine farbige, hier grüne Edge verbunden werden.

![Die Veränderung eines Beispiel Graphen zur Erkennung eines Kondensators - Version 2](.\Dateien\VeraenderungKondensator-2.png){width=50%}

\newpage

Dadurch werden dann nur mehr zwei Kondensatoren gefunden.

![Problem beim plazieren von zwei Kondensatoren nacheinander - Lösung](.\Dateien\ProblemMit2Kond-2.png){width=50%}