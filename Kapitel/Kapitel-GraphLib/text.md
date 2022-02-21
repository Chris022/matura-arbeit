# Graph Library

## Begriffe

### Graph
Ein Graph ist eine Sonderform einer Baum-Datenstruktur.

![Beispiel für einen Graphen](.\Dateien\GraphBild1.png)

Sie besteht aus sogenannten "Vertices"(Singular Vertex) und "Edges".

![Bestandsteile eines Graphen](.\Dateien\GraphBild2.png)

Wobei je ein Vertex einen Datenpunkt repräsentiert,welcher mithilfe einer Edge mit anderen Datenpunkten verbunden ist. Jeder Vertex und jede Edge kann auch noch eine bestimmte Farbe haben. So kann zwischen zwei Strukturen, die zwar strukturell gleich sind, aber je andere Dinge darstellen unterschieden werden.

![Strukturell gleiche Graphen, welche sich lediglich durch die Farbe unterscheiden](.\Dateien\GraphBild3.png) 

In jedem Vertex können hierbei auch unterschiedliche Daten, wie zum Beispiel: Koordinaten gespeichert werden, diese unterscheiden zwei Graphen allerdings **nicht** von einander!

## Problem
Es muss eine Möglichkeit geschaffen werden Graphen zu be- und verarbeiten. Nur so können alle folgenden Schritte einfach und effektiv umgesetzt werden.

## Idee
Eine einfache Bibliothek finden/erstellen.
Diese Bibliothek muss folgende Funktionen bieten:  

* Graphen erstellen
* Graphen Zeichnen
* Einzelne Vertices erstellen und Daten in diesen speichern
* Vertices löschen
* Vertices mit Edges verbinden
* Edges löschen
* Nachbar-Vertices herausfinden (siehe Abbildung:\ref{nachbarVertices})
* Vertices gruppieren und durch einen einzelnen Vertex ersetzen (siehe Abbildung:\ref{verticesGruppieren})
* Einen Vertex zwischen zwei anderen einfügen (siehe Abbildung:\ref{zwischenVertices})
* Zwei Graphen zusammenfügen
* Muster in Graphen zu finden (siehe Abbildung:\ref{musterFinden})


![\label{nachbarVertices}](.\Dateien\NachbarVertices.png){width=40%}

![\label{verticesGruppieren}](.\Dateien\VerticesGruppieren.png){width=40%}

![\label{zwischenVertices}](.\Dateien\VertexZwischeneinfügen.png){width=40%} 

![\label{musterFinden}](.\Dateien\MusterFinden.png){width=70%}

## Umsetzung

### iGraph (Bibliothek)
Zuerst wurde die Bibliothek Graph.io verwendet um mit Graphen zu arbeiten. Ausgewählt wurde dies aufgrund der Verfügbarkeit der Funktion `get_isomorphisms_vf2()`. Diese kann schnell und zuverlässig Muster in Graphen finden.(siehe Erklärung zuvor)  


**Problem:**

1) Die Dokumentation der Bibliothek ist sehr schlecht.
   
2) Außerdem führt ein Löschen von Vertices zu großen Problemen.
   
3) Dadurch sind Funktionen wie "gruppieren", "einfügen von Vertices" nicht umsetzbar.

### Selbst Programmierte Bibliothek

**Lösung:**

Selbst eine Bibliothek entwickeln welche die Probleme von "iGraph", im Austausch zur Geschwindigkeit, beheben. Da die Bibliothek selber in Python entwickelt wurde, ist sie, besonders die äquivalente Funktion zu `get_isomorphisms_vf2()`, nämlich sehr langsam.


**Implementation:**

Im Hintergrund wird ein Graph mithilfe einer Inzidenzmatrix, einer Liste aus Vertex-Objekten und einer Liste aus Edge-Objekten gespeichert.
Eine Inzidenzmatrix ist hierbei eine Tabelle deren Reihe je einen Vertex und deren Spalten je eine Edge beschreiben.

![Beispiel für eine Inzidenzmatrix \label{inzidenzmatrix}](.\Dateien\MatrixErklärung.png){width=70%}

In Beispiel \ref{inzidenzmatrix} sieht man: Vertex "1" ist mit der Edge "1" verbunden. Vertex "2" ist mit Edge "1","2","3" verbunden.

Zum Zeichnen der Graphen wird ein Graph aus unserer Library zuerst in ein xml-encodiertes Text-Dokument umgewandelt. Dieses Dokument wird dann mithilfe von iGraph geöffnet und mit den dadurch zur Verfügung gestellten Funktionen gezeichnet. Dies wurde gemacht da es wesentlich einfach ist, als einen Graph-Zeichen-Algorithmus zu implementieren.

### Wichtige Algorithmen:

**Muster finden:**
Verwendet wurde der so genannte "Ulman's Subgraph Isomorphism Algorithm". Dieser basiert auf darauf, dass grundsätzlich alle Möglichkeiten durchprobiert werden wobei immer im Vorhinein möglichst viele Optionen ausgeschlossen werden!

*Beschreibung des grund-Algorithmus:*

Sein ein Graph H der große Graph und ein zweiter Graph N der Graph der in H gefunden werden soll. H besteht aus |V_H| Vertices und N aus |V_N| Vertices

![Beispiel für 2 Graphen](.\Dateien\Isomothism1.png){width=70%}

1\) Erstelle eine |V_H| x |V_N| Matrix und befülle sie mit 0.

![Leere Matrix für die oben gezeigten Beispiele](.\Dateien\Isomothism2.png){width=20%}

In dieser Matrix bezeichnet eine 1 an der stelle x,y dann dass: der Vertex y in H auf den Vertex x in N passt

![In diesem Fall ist Vertex 1 in N zu Vertex 2 in H geordnet](.\Dateien\Isomothism3.png){width=50%}

2\) Starte mit der ersten Reihe und keiner besuchten Spalte

3\) Prüfe in der gesamten Tabelle pro Spalte **maximal** eine 1 steht und pro Zeile **genau** eine 1 steht. Das heißt jeder Vertex in N ist genau einem Vertex in H zugeordnet.

Wenn Ja)
> Prüfe ob die generierte Zuordnung auch eine mögliche Zuordnung ist und speichere diese, wenn ja!

![Beispiel für eine unmögliche Zuordnung](.\Dateien\Isomothism4.png){width=40%}

Wenn Nein) 

4\) Erstelle Kopie der Tabelle

5\) Für jede noch nicht besuchte Spalte:

   1\) Setze in der derzeitigen Reihe die besuchte Spalte zu 1

   2\) Wiederhole ab Schritt 3) mit:

   * Reihe+1
   * Besuchte Spalten + gerade besuchter
   * Kopie der Tabelle

   3\) Setze die Tabelle wieder zurück


![Beispieldurchgang für einen Stark vereinfachten Graphen und ohne Überprüfung ob es sich um eine mögliche Zuordnung handelt!](.\Dateien\BeschreibungDurchgangBasicSubisomorphismAlgorithm.png)

