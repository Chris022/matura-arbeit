# Umstrukturieren des Graphen

## Problem
Um den Graphen nun besser in ein von Simulatoren verständliches File umzuwandeln muss er zuvor noch Umstrukturiert werden.
Auch müssen alle Bauteile noch neu positioniert werden, um geradlinige Linienführung garantieren zu können.

![Problem mit nicht geradlinigen Linienführungen](.\Dateien\FromTo.png){width=60%}

## Idee
Mithilfe eines Algorithmus soll der Graph so umstrukturiert werden, dass alle Bauteile zu je einem Vertex zusammengefasst werden.

![Umstrukturierung des Graphen](.\Dateien\Umstruckturieren1.png){width=60%}

Mithilfe eines weiteren Algorithmus welcher Bauteil für Bauteil alle Bauteile besucht, sollen jene dann, wie in dem Problem bereits geschrieben, gerade gerichtet werden.

## Umsetzung
