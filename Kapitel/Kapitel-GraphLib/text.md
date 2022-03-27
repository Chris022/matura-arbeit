# Graph Library

## Begriffe

### Graph
Ein Graph ist eine Sonderform einer Baum-Datenstruktur.

![Beispiel für einen Graphen](.\Dateien\GraphBild1.png)

Er besteht aus sogenannten "Vertices"(Knoten) und "Edges"(Kanten), wobei je ein Vertex einen Datenpunkt repräsentiert, welcher mit einem anderen Datenpunkten verbunden ist.

![Bestandsteile eines Graphen](.\Dateien\GraphBild2.png)

Es ist außerdem möglich jedem Knoten und jeder Kante eine eigene Farbe zu geben.So kann zwischen zwei Graphen, die strukturell gleich sind, unterschieden werden.

![Strukturell gleiche Graphen, welche sich lediglich durch die Farbe unterscheiden](.\Dateien\GraphBild3.png) 

In jedem Vertex können hierbei auch unterschiedliche Daten, wie zum Beispiel Koordinaten gespeichert werden. Diese unterscheiden zwei Graphen allerdings **nicht** voneinander!

## Problem
Die gesamte elektronische Schaltung soll später mithilfe eines Graphen dargestellt werden. Dafür ist es nötig, eine Möglichkeit zu schaffen, sehr einfach Graphen zu erstellen und diese weiter zu verarbeiten.

## Idee
Umgesetzt werden sollte dies durch das erstellen/finden einer einfachen Bibliothek zur Graphen Verarbeitung.
Diese Bibliothek muss mindestens folgende Funktionen bieten:  

* Graphen erstellen
* Graphen zeichnen
* Einzelne Vertices erstellen und Daten in diese speichern
* Vertices löschen
* Vertices mit Edges verbinden
* Edges löschen
* Nachbar-Knoten finden (siehe Abbildung \ref{nachbarVertices}: Nachbar-Vertices)
* Vertices gruppieren und durch einen einzelnen Vertex ersetzen (siehe Abbildung \ref{verticesGruppieren}: Vertices-Gruppieren)
* Einen Vertex zwischen zwei anderen einfügen (siehe Abbildung \ref{zwischenVertices} : Zwischen-Vertices)
* Zwei Graphen zusammenfügen
* Muster in Graphen zu finden (siehe Abbildung \ref{musterFinden}: Muster-Finden)


![\label{nachbarVertices}Nachbar-Vertices](.\Dateien\NachbarVertices.png){width=40%}

![\label{verticesGruppieren}Vertices-Gruppieren](.\Dateien\VerticesGruppieren.png){width=40%}

![\label{zwischenVertices}Zwischen-Vertices](.\Dateien\VertexZwischeneinfügen.png){width=40%} 

![\label{musterFinden}Muster-Finden](.\Dateien\MusterFinden.png){width=70%}

## Umsetzung

### iGraph (Bibliothek)
Zuerst wurde die Bibliothek iGraph verwendet, um mit Graphen zu arbeiten. Ausgewählt wurde dies aufgrund der Verfügbarkeit der Funktion `get_isomorphisms_vf2()`. Diese kann schnell und zuverlässig Muster in Graphen finden. (siehe Erklärung zuvor)  


**Problem:**

1) Die Dokumentation der Bibliothek ist sehr schlecht.
   
2) Außerdem führt ein Löschen von Vertices zu großen Problemen.
   
3) Dadurch sind Funktionen wie "gruppieren", "einfügen von Vertices" nicht umsetzbar.

### Selbst programmierte Bibliothek

**Lösung:**

Als Lösung wurde eine eigene Bibliothek entwickelt, welche die Probleme von iGraph behebt. 

**Implementation:**

Im Hintergrund wird ein Graph mithilfe einer Inzidenzmatrix gespeichert.
Eine Inzidenzmatrix ist hierbei eine Tabelle, deren Reihen je einen Vertex und deren Spalten je eine Edge beschreiben.
Eine 1 bei der Edge y und bei dem Vertex x heißt dann einfach, der Vertex x ist mit der Edge y verbunden.

![Beispiel für eine Inzidenzmatrix \label{inzidenzmatrix}](.\Dateien\MatrixErklärung.png){width=70%}

In Abbildung \ref{inzidenzmatrix} sieht man, dass Vertex "1" mit der Kante "1" und Vertex "2" mit den Kanten "1","2" und "3" verbunden ist.

### Weitere wichtige Algorithmen:

#### Zeichnen: 

Zum Zeichnen der Graphen wird ein Graph aus der Bibliothek zuerst in ein xml-encodiertes Text-Dokument umgewandelt. Dieses Dokument wird dann mithilfe von iGraph geöffnet und mit den dadurch zur Verfügung gestellten Funktionen gezeichnet. Dies wurde gemacht, da es wesentlich einfach ist, als einen Graph-Zeichen-Algorithmus zu implementieren.

#### Muster finden:  

Verwendet wurde der sogenannte "Ulman's Subgraph Isomorphism Algorithm". Dieser basiert darauf, dass alle Möglichkeiten durchprobiert werden, bis alle Vorkommen eines Musters in einem Ausgangsgraphen gefunden wurden.

Eine wichtige Rolle spielen hierbei sogenannte "Zuordnungen". Eine Zuordnung ist einfach eine Matrix, welche alle Vertices aus einem Graphen je einen anderen Vertex aus einem anderen Graphen zuordnet.

![Beispiel für eine von mehreren möglichen Zuordnungen. Die jeweiligen Zuordnungen sind gepunktet dargestellt](.\Dateien\Zuordnung.png){width=70%}

*Beschreibung des Grund-Algorithmus:*

Angenommen H ist ein Graph welcher aus |V_H| Knoten besteht und N das Muster aus |V_N| Vertices, welches in H gefunden werden soll.

![Beispiel für zwei Graphen](.\Dateien\Isomothism1.png){width=70%}

1\) Erstelle eine |V_H| x |V_N| Matrix und befülle sie mit 0. In dieser Matrix bezeichnet eine 1 an der Stelle (x,y) dass, der Vertex x in H, dem Vertex y in N zugeordnet wird

![Leere Matrix für die oben gezeigten Beispiele](.\Dateien\Isomothism2.png){width=20%}


![In diesem Fall ist Vertex 1 in N, Vertex 2 in H zugeordnet](.\Dateien\Isomothism3.png){width=50%}

2\) Befülle die Matrix an allen Stellen mit 1, an denen eine Zuordnung möglich ist. Das bedeutet (x,y) ist 1 wenn Vertex x in H einem Vertex y in N zugeordnet werden kann!

3\) Starte in der ersten Reihe der Matrix und mit noch keiner besuchten Spalte.

4\) Prüfe ob in der gesamten Tabelle pro Spalte **maximal** eine 1 steht und pro Zeile **genau** eine 1 steht. Das heißt, jeder Vertex in N ist genau einem Vertex in H zugeordnet.

Wenn Ja)
>Wenn die generierte Zuordnung auch eine mögliche ist, speichere sie.
Wenn Nein) 

5\) Erstelle eine Kopie der Matrix

6\) Für jede noch nicht besuchte Spalte, besuche Spalte:

6.1\) Prüfe ob der Wert in der Matrix an der derzeitigen Reihe und gerade besuchten Spalte 1 is. Wenn nein, überspringe die Spalte

6.2\) Sei die derzeit besuchte Spalte x und die derzeit besuchte Reihe y, setze (x,y) zu 1

6.3\) Wiederhole ab Schritt 3) mit:

   * Reihe+1
   * Besuchte Spalten + gerade besuchter Spalte
   * Kopie der Tabelle

6.4\) Setze die Tabelle wieder zurück


![Beispieldurchgang für einen stark vereinfachten Graphen. In diesem Beispiel beginnt der Algorithmus mit einer ganz leeren Matrix anstelle einer bereits zum Teil gefüllten! Es wird dementsprechend also auch Schritt 2) ausgelassen](.\Dateien\BeschreibungDurchgangBasicSubisomorphismAlgorithm.png)

***

*Beschreibung der Verbesserung*  

Da der Algorithmus, wie er oben beschrieben ist, noch extrem langsam ist, gibt es einen zusätzlichen Schritt zwischen 4) und 5) um einige Zuordnungen dirket auszuschließen!

![Beispiel für Überprüfung. Die Zuordnung ist dabei gepunktet](.\Dateien\Vereinfachung0.png){width=60%}

Für jeden Vertex in N suche den zugeordneten Vertex aus H.

![Suche den zugeordneten Vertex für 1](.\Dateien\Vereinfachung1.png){width=60%}

Suche die Nachbarn für beide Vertices.

![Suche die Nachbarn (hier grau)](.\Dateien\Vereinfachung2.png){width=60%}

Für jeden Nachbar des N-Vertex, suche dessen zugeordneten H-Vertex.
Nur wenn mindestens einer davon auch ein Nachbar des ursprünglichen Vertex aus H ist, ist eine Zuordnung möglich

![Zuordnung von 1 auf 2 ist in diesem Fall somit möglich!](.\Dateien\Vereinfachung3.png){width=60%}


Dies wird solange wiederholt, bis die Matrix nicht mehr verändert wurde.


***

*Beschreibung des Algorithmus zur Prüfung, ob eine Zuordnung möglich ist \label{möglicheZuordnung}*  

Suche für jeden Vertex aus N den zugeordneten Vertex aus H. Wenn beide nicht die gleiche Farbe haben oder wenn der Vertex aus H weniger Nachbarn hat als der aus N, dann ist keine Zuordnung möglich.

![1 und 1 werden nie zuordenbar sein, da sie unterschiedliche Farbe haben und H1 nur einen Nachbar hat, N1 aber mindestens zwei benötigt](.\Dateien\Zuordnungsbarkeit.png){width=50%}

***


*Beischreibung der Überprüfung, ob es sich um eine mögliche Zuordnung handelt \label{validIsomophism}*  

Die Idee ist es, aus einer Zuordnung und aus dem Graphen H einen neuen Graph zu generiert. Ist dieser Graph gleich dem Graphen N, so handelt es sich um eine valide Zuordnung!

![Beispiel für eine unmögliche Zuordnung](.\Dateien\Isomothism4.png){width=40%}

Dafür werden die Graphen H und N in eine sogennante Adjacency-Matrix umgewandelt. Anschließend rechnet man $M(MH)^T == N$ wobei M die Zuordnungsmatrix ist

Graphisch representiert diese Rechnung folgendes:

![Beispiel Graphen](.\Dateien\isValidSumgraph0.png){width=55%}

**Schritt 1**

![Alle Verbindungen nach 1 werden ausgetauscht mit Verbindungen nach Zuweisung(1) = 1](.\Dateien\isValidSumgraph1.png){width=50%}

\newpage
**Schritt 2**

![Alle Verbinungen nach 2 werden mit Verbindungen nach Zuweisung(2) = Keine](.\Dateien\isValidSumgraph2.png){width=50%}

**Schritt 3**

![Alle Verbinungen nach 3 werden mit Verbindungen nach Zuweisung(3) = 2](.\Dateien\isValidSumgraph3.png){width=50%}

**Schritt 4**

![Alle Verbinungen nach 4 werden mit Verbindungen nach Zuweisung(4) = Keine](.\Dateien\isValidSumgraph4.png){width=50%}

**Schritt 5**

![Alle Vertices die nicht in N vorkommen werden entfernt](.\Dateien\isValidSumgraph5.png){width=35%}

\newpage
**Schritt 6**

![Sind die Geraphen gleich? Nur wenn ja, ist eine Zuordnung möglich. In diesem speziellen Fall sind die Graphen gleich, wodurch eine Zuordnung möglich ist.](.\Dateien\isValidSumgraph6.png){width=50%}