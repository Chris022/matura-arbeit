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

#### Muster finden:  

Verwendet wurde der so genannte "Ulman's Subgraph Isomorphism Algorithm". Dieser basiert auf darauf, dass grundsätzlich alle Möglichkeiten durchprobiert werden wobei immer im Vorhinein möglichst viele Optionen ausgeschlossen werden!
Ein Muster nennt man hierbe, mit Fachausdruck auch Subgraph. 


*Beschreibung des grund-Algorithmus:*

Sei H der große Graph und N ein zweiter Graph der in H gefunden werden soll. H besteht aus |V_H| Vertices und N aus |V_N| Vertices

![Beispiel für 2 Graphen](.\Dateien\Isomothism1.png){width=70%}

1\) Erstelle eine |V_H| x |V_N| Matrix und befülle sie mit 0.

![Leere Matrix für die oben gezeigten Beispiele](.\Dateien\Isomothism2.png){width=20%}

In dieser Matrix bezeichnet eine 1 an der stelle x,y dann dass: der Vertex y in H auf den Vertex x in N passt

![In diesem Fall ist Vertex 1 in N zu Vertex 2 in H geordnet](.\Dateien\Isomothism3.png){width=50%}

2\) Befülle die Matrix an allen stellen mit 1, in denen eine Zuordnung möglich wäre. Also für jeden Vertex aus H prüfe für jeden Vertex aus N ob eine Zuordnung möglich wäre und setzte jene Stelle in der Matrix zu 1. Für die Überprüfung verwende unten beschriebenen Algorithmus zur "Überprüfung der Zuordnungbarkeit" 

3\) Starte mit der ersten Reihe und keiner besuchten Spalte

4\) Prüfe in der gesamten Tabelle pro Spalte **maximal** eine 1 steht und pro Zeile **genau** eine 1 steht. Das heißt jeder Vertex in N ist genau einem Vertex in H zugeordnet.

Wenn Ja)
> Prüfe ob die generierte Zuordnung auch einen möglichen Subgraphen generiert(laut Algorithmus später). Speichere die Zuordnung wenn ja

![Beispiel für eine unmögliche Zuordnung](.\Dateien\Isomothism4.png){width=40%}

Wenn Nein) 

5\) Erstelle Kopie der Tabelle

6\) Für jede noch nicht besuchte Spalte:

   1\) Prüfe ob der Wert in der Tabelle an der derzeitigen Reihe und gerade besuchten Spalte 1 is. Wenn nicht überspringe die Spalte

   2\) Setze in der derzeitigen Reihe die besuchte Spalte zu 1 den Rest zu 0

   3\) Wiederhole ab Schritt 3) mit:

   * Reihe+1
   * Besuchte Spalten + gerade besuchter
   * Kopie der Tabelle

   3\) Setze die Tabelle wieder zurück


![Beispieldurchgang für einen Stark vereinfachten Graphen und ohne Überprüfung ob es sich um eine mögliche Zuordnung handelt! Außerdem beginnt dieser Algorithmus mit einer ganz leeren Matrix anstelle einer bereits zum teil gefüllten! Es wird dementsprechend also auch Schritt 1) ausgelassen](.\Dateien\BeschreibungDurchgangBasicSubisomorphismAlgorithm.png)

***

*Beschreibung des Algorithmus zur Prüfung ob es sich um eine mögliche Zuordnung handelt*  

Prüfe ob ein Vertex aus H die gleiche Farbe wie der aus N hat. Wenn nicht -> keine Zuordnung möglich  
Prüfe ob der sogenannte "degree" des Vertex aus H größer gleich dem aus N ist. Der "degree" beschreibt hierbei die Anzahl an Nachbarn die ein Vertex hat. Hat nu ein Vertex in H nur 2 Nachbarn, einer in N aber 3, so werden die zwei Vertices niemals zuordenbar werden!

![1 und 1 werden nie zuordenbar sein, da sie unterschiedliche Farbe haben und H1 nur einen Nachbar hat, N1 aber mindestens zwei benötigt](.\Dateien\Zuordnungsbarkeit.png){width=50%}

***

*Beschreibung der Verbesserung*  

Da der Algorithmus wie er oben beschrieben ist noch extrem langsam ist, gibt es einen zusätzlichen Schritt zwischen 4) und 5) um einige zuordnungs Möglichkeiten dirket auszuschließen! Dies geschieht dadurch, dass gewisse Zellen in der Tabelle zu 0 gemacht werden und somit in weitere Folge übersprungen werden.

Dafür werden für jede Zelle die Nachbarn des entsprechenden N-Vertex geholt.
Genau so werden für jede Zelle die Nachbarn des entsprechenden H-Vertex geholt.
Ein Zuordnen ist nur möglich wenn alle Nachbarn des N-Vertex auch zuweisbar auf mindestens einen Nachbar des H-Vertex sind!
Dies wird solange wiederholt bis die Matrix nicht mehr verändert wurde.

![Einzelne Wiederholung des Vereinfachungs-Algorithmus](.\Dateien\AlgorithmusSimplyfiy.png){width=60%}

***

*Beischreibung der Überprüfung ob es sich um einen möglichen Subgraphen handelt*  

Die Idee ist folgende: Es wird aus einer Zuordnung und aus dem Graphen H ein neuer Graph generiert. Ist dieser Graph gleich dem Graphen N, so handelt es sich um einen validen Subgraphen!

Dafür werden die Graphen H und N in eine Adjacency-Matrix umgewandelt. Anschließend rechnet man: $$M(MH)^T == N$$ wobei M die Zuordnungsmatrix ist

Graphisch representiert diese Rechnung folgendes:

![Beispiel Graphen](.\Dateien\isValidSumgraph0.png){width=50%}

Schritt 1

![Alle Verbindungen nach 1 werden ausgetauscht mit Verbindungen nach Zuweisung(1) = 1](.\Dateien\isValidSumgraph1.png){width=30%}

Schritt 2

![Alle Verbinungen nach 2 werden mit Verbindungen nach Zuweisung(2) = None](.\Dateien\isValidSumgraph2.png){width=30%}

Schritt 3

![Alle Verbinungen nach 3 werden mit Verbindungen nach Zuweisung(3) = 2](.\Dateien\isValidSumgraph3.png){width=30%}

Schritt 4

![Alle Verbinungen nach 4 werden mit Verbindungen nach Zuweisung(4) = None](.\Dateien\isValidSumgraph4.png){width=30%}

Schritt 5

![Alle Vertices die nicht in N vorkommen werden entfernt](.\Dateien\isValidSumgraph5.png){width=15%}

Schritt 6

![Sind die Geraphen gleich?](.\Dateien\isValidSumgraph6.png){width=50%}