# Finden der Bauteile

## Problem
Damit später die Bauteile in ein Simulationsprogramm eingefügt werden können muss als erstes die Position der Bauteile innerhalb der Schaltung gefunden werden. 

## Idee
In dem Graph sucht man nach bestimmten Mustern, welche ein Bauteil darstellen. Dadurch dass dann in jedem Vertex im Graph die original Koordinaten gespeichert sind, kann dann die Positon des jeweiligen Bauteils im Ausgangsbild gefunden werden.

## Umsetzung

Im Graphen, ist jedes Bauteil relativ leicht anhand seines Musters zu idendifizieren.

![Muster für ein Gnd Symbol im Graphen](.\Dateien\MusterGnd.png)

![Muster für einen Widerstand im Graphen](.\Dateien\MusterWiderstand.png)

Mithilfe der Muster-Findungs-Funktion die unsere Graph Bibliothek zur Verfügung stellt, können die Muster dann sehr leicht gefunden werden. Wichtig ist, dass es in diesem Schritt lediglich wichtig ist, die Position der Bauteile zu finden, nicht die art des Bauteils.