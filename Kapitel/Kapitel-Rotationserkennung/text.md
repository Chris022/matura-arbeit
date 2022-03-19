# Rotationserkennung

## Problem

Nachdem alle Bauteile Klassifiziert wurden, muss für jedes Bauteil noch festgestellt werden in welche richtung (horizontal oder vertikal) es gedreht ist, damit das Bauteil in LTspice richtig gezeichnet werden kann.

## Idee

## Rotationserkennung mit Neuronalem Netzwerk

Dass Neuronale Netzwerk, welches darauf trainiert wurde die Bauteile zu klassifizieren sollte zusätlich noch die Rotation jedes Bauteils herausfinden.

Genauer?

Diese Mehtode der Rotationserkennung war jedoch sehr ungenau, weshaöb eine andere Methode gewählt wurde.


## Umsetzung 

Der Funktion, welche die Rotation erkennen soll, wird eine Liste mit allen Vertices des Bauteils übergeben.

![Graph eines Widerstandes](.\Dateien\resistorpattern.png){width=50%}

Aus dieser Liste werden alle Intersection Vertices herausgesucht. Danach wird jeweils der Abstand der beiden Vertices in X-Richtung und Y-Richtung berechnet. Ist der horizontale Abstand größer, ist das Bauteil horizontal gezeichnet ansonsten vertikal.

![Abstände zwischen den Vertices](.\Dateien\dxdy.png){width=50%}