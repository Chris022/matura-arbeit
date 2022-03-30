# Rotationserkennung

## Problem

Nachdem alle Bauteile klassifiziert wurden, muss für jedes Bauteil noch festgestellt werden in welche Richtung (horizontal oder vertikal) es gedreht ist, damit das Bauteil in LTspice richtig gezeichnet werden kann.

## Rotationserkennung mit Neuronalem Netzwerk

Das Neuronale Netzwerk, welches darauf trainiert wurde, die Bauteile zu klassifizieren, sollte zusätzlich noch die Rotation jedes Bauteils herausfinden. 

Dafür wurde der Output Layer des Netzwerkes um vier Neuronen erweitert, welche jeweils für eine Richtung stehen. Als Richtung wurde das Neuron mit der höchsten Aktivierung verwendet.

Diese Mehtode der Rotationserkennung war jedoch sehr ungenau, da die Ausgabe des Neuronalen Netzwerkes oft falsch war.
Deshalb wurde eine andere Methode zur Erkennung der Rotation gewählt.


## Umsetzung 

Der Funktion, welche die Rotation erkennen soll, wird eine Liste mit allen Vertices des Bauteils übergeben.

![Graph eines Widerstandes](.\Dateien\resistorpattern.png){width=50%}

Aus dieser Liste werden alle Intersection Vertices herausgesucht. Danach wird jeweils der Abstand der beiden Vertices in X-Richtung und Y-Richtung berechnet. Ist der horizontale Abstand größer, ist das Bauteil horizontal gezeichnet ansonsten vertikal.

![Abstände zwischen den Vertices](.\Dateien\dxdy.png){width=50%}