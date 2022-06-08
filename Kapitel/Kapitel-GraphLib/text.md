# Graph Library

## Begriffe

### Graph
Ein Graph ist eine Sonderform einer Baum-Datenstruktur.

![Beispiel für einen Graphen](.\Dateien\GraphBild1.png)

Er besteht aus sogenannten "Vertices"(Knoten) und "Edges"(Kanten), wobei je ein Vertex einen Datenpunkt repräsentiert, welcher mit einem anderen Datenpunkt verbunden ist.

![Bestandsteile eines Graphen](.\Dateien\GraphBild2.png)

Außerdem ist es möglich, jedem Knoten und jeder Kante eine eigene Farbe zu geben. So kann auch zwischen zwei Graphen, die strukturell gleich sind, unterschieden werden.

![Strukturell gleiche Graphen, welche sich lediglich durch die Farbe unterscheiden](.\Dateien\GraphBild3.png) 

In jedem Vertex können hierbei auch unterschiedliche Daten, wie zum Beispiel Koordinaten gespeichert werden. Diese unterscheiden zwei Graphen allerdings **nicht** voneinander!

\newpage
### Inzidenzmatrix

Eine Inzidenzmatrix ist eine Tabelle, deren Spalten für die einzelnen Edges und deren Reihen für je einen Vertex stehen.
Besitzt diese Tabelle nun an der Stelle [X,Y] eine 1, so bedeutet dies, dass Vertex Y mit der Edge X Verbunden ist.

![Beispiel für eine Inzidenzmatrix \label{inzidenzmatrix}](.\Dateien\MatrixErklärung.png){width=70%}

In Abbildung \ref{inzidenzmatrix} sieht man, dass Vertex "1" mit der Kante "1" und Vertex "2" mit den Kanten "1", "2" und "3" verbunden ist.

\newpage

### Zuordnung/Zuordnungs-Matrix

Eine Zuordnung ist eine Matrix, welche alle Vertices aus einem Graphen je einen anderen Vertex aus einem anderen Graphen zuordnet. Eine sole Zuordnungsmatrix ist dabei nur valide, wenn pro Spalte **maximal** eine 1 steht und pro Zeile **genau** eine 1 steht. Das heißt, jeder Vertex ist **genau** einem anderen Vertex zugeordnet.

![Beispiel für eine von mehreren möglichen Zuordnungen. Die jeweiligen Zuordnungen sind gepunktet dargestellt.\label{zuordnung}](.\Dateien\Zuordnung.png){width=70%}

In Abbildung \ref{zuordnung} sieht man, dass zum Beispiel Vertex "1" aus dem rechten Graphen, dem Vertex "2" aus dem linken zugeordnet wird.

Wichtig hierbei ist, dass eine Zuordnung sowohl "möglich" also auch "unmöglich" sein kann.

![Beispiel für eine unmögliche Zuordnung](.\Dateien\BeispielFürEineUnmöglicheZuordnung.png){width=40%}

![Beispiel für eine mögliche Zuordnung](.\Dateien\BeispielFürEineMöglicheZuordnung.png){width=40%}

## Problem
Die gesamte elektronische Schaltung soll später mithilfe eines Graphen dargestellt werden. Dafür muss eine Möglichkeit geschaffen werden, sehr einfach Graphen zu erstellen und diese weiter zu verarbeiten.

\newpage

## Idee
Umgesetzt werden sollte dies durch das Erstellen bzw. Finden einer einfachen Bibliothek zur Graphenverarbeitung.
Diese Bibliothek muss mindestens folgende Funktionen bieten:  

* Graphen erstellen
* Graphen zeichnen
* Einzelne Vertices erstellen und Daten in diese speichern
* Vertices löschen
* Vertices mit Edges verbinden
* Edges löschen
* Nachbar-Knoten finden (siehe Abbildung \ref{nachbarVertices}: Nachbar-Vertices)
* Vertices gruppieren und durch einen einzelnen Vertex ersetzen (siehe Abbildung \ref{verticesGruppieren}: Vertices gruppieren)
* Einen Vertex zwischen zwei anderen einfügen (siehe Abbildung \ref{zwischenVertices} : Zwischenvertices)
* Zwei Graphen zusammenfügen
* Muster in Graphen zu finden (siehe Abbildung \ref{musterFinden}: Muster finden)


![\label{nachbarVertices}Nachbar-Vertices](.\Dateien\NachbarVertices.png){width=30%}

![\label{verticesGruppieren}Vertices gruppieren](.\Dateien\VerticesGruppieren.png){width=40%}

![\label{zwischenVertices}Zwischenvertices](.\Dateien\VertexZwischeneinfügen.png){width=40%} 

![\label{musterFinden}Muster finden](.\Dateien\MusterFinden.png){width=70%}

## Umsetzung

### iGraph (Bibliothek)
Zuerst wurde die Bibliothek iGraph verwendet. Ausgewählt wurde sie aufgrund der Verfügbarkeit der Funktion `get_isomorphisms_vf2()`. Diese kann schnell und zuverlässig Muster in Graphen finden. (siehe Erklärung zuvor)  


**Problem:**

1) Die Dokumentation der Bibliothek ist sehr schlecht.
   
2) Außerdem führt ein Löschen von Vertices zu großen Problemen.
   
3) Dadurch sind Funktionen wie "Gruppieren" oder "Einfügen von Vertices" nicht umsetzbar.

### Selbst programmierte Bibliothek

**Lösung:**

Als Lösung wurde eine eigene Bibliothek entwickelt, welche die Probleme von iGraph behebt. 

**Implementierung:**

Im Hintergrund wird ein Graph mithilfe einer Inzidenzmatrix gespeichert. Zusätzlich ist jeder Vertex und jede Edge als Objekt in je einer Vertex- bzw. Edge-Liste gespeichert. Der jeweilige Index in der Liste korrespondiert mit der jeweiligen Spalte oder Reihe.

\newpage

### Wichtige Algorithmen:

#### Zeichnen: 
\
Zum Zeichnen der Graphen wird ein Graph Objekt zuerst in ein xml-encodiertes Text-Dokument umgewandelt. Dieses Dokument wird dann mithilfe von iGraph geöffnet und mit den dadurch zur Verfügung gestellten Funktionen gezeichnet. Dies ist wesentlich einfacher, als einen Graph-Zeichen-Algorithmus selbst zu implementieren. Außerdem wird diese Funktion nur zum Debugen benötigt, und somit können in diesem Fall die Problemen von iGraph ignoriert werden.



#### Muster finden:
\
Verwendet wurde der sogenannte "Ulman's Subgraph Isomorphism Algorithm".

Dieser basiert darauf, dass alle möglichen Zuordnungen durchprobiert werden.
Ist H also ein Graph, welcher aus |V_H| Knoten besteht und N das Muster aus |V_N| Vertices, welches in H gefunden werden soll,
dann einfach alle Permutationen mit |V_N| Vertices  im Graphen H generiert.

**Beispiel**:

* H besitzt folgende Vertices: [A,B,C]
* G besteht aus diesen Vertices: [1,2]
* Zuerst werden alle Permutationen generiert: [A,B],[A,C],[B,C]
* Anschließend werden alle nicht möglichen Permutationen entfernt.

![Graphische Darstellung des Beispiels](.\Dateien\GrundkonzeptUlmans.png){width=50%}

Diese Erklärung ist stark vereinfacht und in Wirklichkeit werden auch keine Permutationen sondern Zurodnungs-Matrizen generiert, trotzdem ist das Beispiel zur Erklärung des Grundkonzeptes sehr gut geeignet. Im folgenden wird der Algorithmus noch  genauer erklärt.

\newpage


\underline{Algorithmus zur Überprüfung, ob ein Vertex aus dem Graphen N}
\underline{einem Vertex aus dem Graphen H zugeordnet werden kann:}
\label{möglicheZuordnung}

**Prüfe**, ob der Vertex aus N die gleiche Farbe hat wie Vertex aus Graph H. \
Wenn Nein: \
&nbsp;&nbsp;&nbsp; *Kann nicht zugeordnet werden* \
**Prüfe**, ob der Vertex aus N mehr Nachbarn hat als der Vertex aus H \
Wenn Ja: \
&nbsp;&nbsp;&nbsp; *Kann nicht zugeordnet werden* \
Sonst: \
&nbsp;&nbsp;&nbsp; *Kann zugeordnet werden* \

Beispiel:

!["H1" und "N1" werden nie zuordenbar sein, da sie unterschiedliche Farben haben und H1 nur einen Nachbar hat, N1 aber mindestens zwei benötigt](.\Dateien\Zuordnungsbarkeit.png){width=50%}

\newpage

\underline{Algorithmus zur Überprüfung, ob eine Zuordnung möglich ist:}

Die Idee ist, aus einer Zuordnung und dem Graphen H einen neuen Graph zu generiert. Ist dieser Graph gleich dem Graphen N, so handelt es sich um eine valide Zuordnung!


Dafür werden die Graphen H und N in eine sogennante Adjacency-Matrix umgewandelt. Anschließend rechnet man $M(MH)^T == N$ wobei M die Zuordnungsmatrix ist

Im Graphen repräsentiert diese Rechung folgendes:

**Wiederhole** für jeden Vertex in H \
&nbsp;&nbsp;&nbsp; **Prüfe** auf welchen Vertex in N der gerade besuchte Vertex in H zugeordnet wird. \
&nbsp;&nbsp;&nbsp; **Entferne** alle Edges, die mit dem gerade besuchten Vertex in H verbunden sind. \
&nbsp;&nbsp;&nbsp; **Verbinde** dies Edges stattdessen mit dem Vertex, dem der gerade besuchte zugeordnet ist. Sollte er keinem \
&nbsp;&nbsp;&nbsp; zugeordnet sein, lösche die Edges. \
**Entferne** alle Vertices, die nicht in Graph N vorkommen. \
**Prüfe**, ob der ursprüngliche Graph N und der neu generierte Graph gleich sind \
Wenn Ja: \
&nbsp;&nbsp;&nbsp; *es handelt sich um eine mögliche Zuordnung* \
Sonst: \
&nbsp;&nbsp;&nbsp; *es handelt sich um eine unmögliche Zuordnung* \

**Erklärung anhand eines Beispiels**:

In diesem Beispiel soll überprüft werden, ob die Zuordnung von Vertex "1N" auf Vertex "1H" und die Zuordnung von Vertex "2N" auf Vertex "3H", eine mögliche Zuordnung ist.

![Beispiel Graphen](.\Dateien\isValidSumgraph0.png){width=55%}


**Schritt 1**

![Alle Verbindungen nach "H1" werden ausgetauscht mit Verbindungen nach Zuordnung("H1") = "N1".](.\Dateien\isValidSumgraph1.png){width=50%}

**Schritt 2**

![Alle Verbinungen nach "H2" werden mit Verbindungen nach Zuordnung("H2") = Keine](.\Dateien\isValidSumgraph2.png){width=50%}


**Schritt 3**

![Alle Verbinungen nach "H3" werden mit Verbindungen nach Zuordnung("H3") = "N2"](.\Dateien\isValidSumgraph3.png){width=50%}

**Schritt 4**

![Alle Verbinungen nach "H4" werden mit Verbindungen nach Zuordnung("H4") = Keine](.\Dateien\isValidSumgraph4.png){width=50%}

\newpage

**Schritt 5**

![Alle Vertices die nicht in N vorkommen werden entfernt](.\Dateien\isValidSumgraph5.png){width=35%}

**Schritt 6**

![Sind die Geraphen gleich? Nur wenn ja, ist eine Zuordnung möglich. In diesem speziellen Fall sind die Graphen gleich, wodurch eine Zuordnung möglich ist.](.\Dateien\isValidSumgraph6.png){width=50%}


\newpage

\underline{Algorithmus zum Finden der Muster}

**Erstelle** eine |V_H| x |V_N| Zuordnungs-Matrix. \
**Befülle** sie mit 0. \
**Befülle** die Matrix an der Stelle (x,y) mit 1, wenn Vertex x aus Graph H dem Vertex y aus N zugeordnet werden kann. Überprüfung erfolgt mittels des vorher beschriebenen Algorithmus (Algorithmus zur Überprüfung, ob ein Vertex aus dem Graphen N einem Vertex aus dem Graphen H zugeordnet werden kann.) \
**Initialisiere** einen Reihen-Zäler mit 0. \
**Initialisiere** einen leeren Spalten-Array. \

\setlength{\fboxsep}{0pt}
\colorbox{blue!30}{Rekursiver Teil}: \
**Prüfe**, ob es sich um eine valide Zuordnung handelt. (Pro Spalte **maximal** eine 1 steht und pro Zeile **genau** eine 1 steht) \
Wenn Ja: \
&nbsp;&nbsp;&nbsp; **Prüfe** laut Algorithmus "Algorithmus zur Überprüfung, ob eine Zuordnung möglich ist", ob die Zuordnung \
&nbsp;&nbsp;&nbsp; eine mögliche ist. \
&nbsp;&nbsp;&nbsp; Wenn Ja: \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Speichere** die Zuordnung. \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Beende** diesen Ast der Rekursion = **Return** \
\colorbox{yellow!30}{Möglichkeit für Verbesserung} \
**Erstelle** eine Kopie der Matrix \
**Finde** alle Spalten in der kopierten Matrix, die nicht im Spalten-Array gespeichert sind \
**Wiederhole** für jede der Spalten \
&nbsp;&nbsp;&nbsp; **Prüfe**, ob der Wert in der Spalte, auf den der Reihen-Zähler zeigt, 1 ist \
&nbsp;&nbsp;&nbsp; Wenn Nein: \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Überpringe** die Spalte \
&nbsp;&nbsp;&nbsp; **Setze** den Wert in der Spalte, auf den der Reihen-Zähler zeigt, zu 1 \
&nbsp;&nbsp;&nbsp; **Erhöhe** den Reihenzähler um eins \
&nbsp;&nbsp;&nbsp; **Füge** die gerade besuchte Spalte zum Spalten-Array hinzu \
&nbsp;&nbsp;&nbsp; **Wiederhole** den \colorbox{blue!30}{rekursiven Teil} \
&nbsp;&nbsp;&nbsp; **Veringere** den Reihenzähler um eins \
&nbsp;&nbsp;&nbsp; **Entferne** die gerade besuchte Spalte aus dem Spalten-Array \

\newpage

**Erklärung anhand eines Beispiels**:

![Beispieldurchgang für einen stark vereinfachten Graphen. In diesem Beispiel beginnt der Algorithmus mit einer ganz leeren Matrix anstelle einer bereits zum Teil gefüllten!](.\Dateien\BeschreibungDurchgangBasicSubisomorphismAlgorithm.png)

<!--
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

-->

\newpage

\underline{Beschreibung der Verbesserung}

Da der Algorithmus, wie er oben beschrieben ist, noch extrem langsam ist, gibt es einen zusätzlichen Schritt, welcher an der oben gelb makierten Stelle eingefügt werden kann.
Dieser Schritt erlaubt es, einige Zuordnungen dirket auszuschließen, wodurch ein gesammter "rekursiver Ast" wegfällt.

Grundsätzlich gilt also, je früher eine Zuordung ausgeschlossen werden kann, desto performanter wird der Algorithmus.

**Wiederhole** solange bis die Matrix nicht mehr verändert wurde. \
&nbsp;&nbsp;&nbsp; **Wiederhole** für jeden Vertex im "Muster-Graph" \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Suche** den zugeordneten Vertex im anderen Graphen \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Finde** die Nachbarn beider Vertices \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Prüfe** ob mindestens ein Nachbar des einen Vertex auch einem Nachbar des anderen Vertex zugeordnet werden \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; kann! \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Wenn dies nicht der Fall ist: \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Setze** den Wert in der Matrix, welcher für den geraden besuchten Vertex im "Muster-Graph" und dem ihm \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; zugeordneten Vertex im anderen Graphen steht, zu 0 \

**Erklärung anhand eines Beispiels**:

![Für jeden Vertex in N suche den zugeordneten Vertex aus H](.\Dateien\Vereinfachung0.png){width=60%}

![Suche den zugeordneten Vertex für "N1"](.\Dateien\Vereinfachung1.png){width=60%}

\newpage

![Suche die Nachbarn für beide Vertices. (hier grau)](.\Dateien\Vereinfachung2.png){width=60%}

![H3 kann auf "N3" zugeordnet werden, also ein Nachbar von "H2" kann auf einen Nachbar von "N1" zugeordnet werden. Somit ist die Zuordnung von "H2" auf "N1" grundsätzlich möglich und es kann keine Vereinfachung getroffen werden.](.\Dateien\Vereinfachung3.png){width=60%}
