# Bauteilklassifizierung

## Problem

Um die Schaltung zu digitalisieren, müssen alle Bauteile, nach dem deren Position gefunden worden ist, noch richtig erkannt werden.

## Idee

Um die Bauteile zu erkennen soll ein "Convolutional Neural Network" verwendet werden.

![Funktion CNN](.\Dateien\cnn.png){width=70%}

Diesem Netzwerk wird das Bild eines Bauteiles übergeben und als Antwort erhählt um welches Bauteil es sich am wahrscheinlichsten handelt.

## Neuronales Netzwerk

Ein Neuronales Netzwerk ist ein Algorithmus der dem Menschlichem Gehirn nachempfunden ist. Solche Netzwerke können verwendet werden, um Muster in Daten zu finden, wie zum Beispiel gegenständen auf Bildern zu erkennen.

### Aufbau

Ein Neuronales Netzwerk besteht aus Neuronen, die in mehreren Schichten (Layer) angeordnet sind. Jedes Netzwerk hat am Anfang einen Input Layer sowie am Ende einen Output Layer. Zwischen diesen beiden Layer können einer oder mehrere Hidden Layer liegen.

![Struktur eines Neuronalen Netzwerkes](.\Dateien\aufbauNN.png){width=70%}

Jedes Neuron einthält eine Nummer auch Aktivierung genannt.

Um Bauteile einer Schaltung zu erkennen, würde die Aktivierung der Neuronen im input Layer jeweils der Pixelwert eines Bildes sein.

![Input Layer eines Neuronalen Netzwerkes](.\Dateien\inputLayer.png){width=70%}

Die Länge des Output Layers wäre die Anzahl der verschiedenen Bauteile die dieses Netzwerk erkennen kann. Dabei ist die Aktivierung eines Neurons am Ausgang die jeweilige wahrscheinlichkeit, dass auf dem bild das jeweilige Bauteil abgebildet ist. 

![Output Layer eines Neuronalen Netzwerkes](.\Dateien\outputLayer.png){width=70%}


Alle Neuronen in einem Layer sind mit keweils allen Neuronen aus dem vorherigen Layer über Gewichte (weights) verbunden und besitzten einen Schwellwert (bias).


Um die Aktivierung eines Neurons zu berechne wird zuerst die Gewichtete Summe berechnet. Für die Gewichtete Summe z wird jeder Eingang x mit seinem jeweiligen Gewicht w multiplieziert und diese werden mit dem bias  des Neurons addiert. Die Gewichtete Summe wird zum Schluss in eine Funktion (Activation function) gegeben, der Funktionswert entspricht der Aktivierung.

![Aktivierung eines Neurons](.\Dateien\singleNeuron.png){width=70%}

In einem Neuronalen Netzwerk sind die Eingänge x jeweils die Aktivierung aus dem vorherigen Layer.

![Berechnung der Aktivierung in einem Netzwerk](.\Dateien\calculate.png){width=70%}

### Trainieren eines Neuronalen Netzwerkes

Die Gewichte und Schwellwerte eines Neuronalen Netzwerkes können mithilfe eines Algorithmus "erlernt" werden.
Dafür wird eine große Anzahl an Trainingsdaten benötigt. Das sind Daten bei denen der gewünschte Ausgabewert bereits bekannt ist. 

Zuerst werden die Gewichte und Schwellwerte zufällig gewählt. Danach wird die Ausgabe des Netzwerkes für ein Trainingsbild mit dem gewünschten Ausgabewert verglichen und es kann somit festgestellt werden wie gut das Netzwerk fuktioniert. Die Gewichte werden daraufhin so verändert, dass die Ausgabe des Netzwerkes sich dem gewünschten Ausgabewert annähert. Dies wird für alle Trainingsdaten so lange wiederholt, bis Ausgabe des Netzwerkes mit den gewünschten Ausgabewerten annähernd übereinstimmt.

![Ausgabe und gewünschte Ausgabe](.\Dateien\loss.png){width=30%}


## Convolutional Neural Network

Ein Convolutional Neural Network besitzt im gegensatz zu einem Neuronalen Netzwerk mehr verschiedene Layer.


### Filter

Bei einem Convolutional Layer werden ein oderer mehrere Filter verwendet.

Diese Filter werden dabei über das Bild geschoben und die darunter liegenden Werte werden mit den Filterwerten multipliziert und addiert. Der resultierende wert wir darauf hin in einer sogennante "Feature map" gespeichert.

### Beispiel Filter

Bei diesem Beispiel wird ein Filter verwendet um eine spezielle Ecke zu erkennen. Je höher der Wert in der Feature map desto höher ist die übereinstimmung. 

![Beispiel Filter zur erkennung von Ecken](.\Dateien\filter.png){width=70%}

### Convolutional Layer

Ein Convolutional Layer besteht meist aus mehreren Filtern die eine vielzahl an Feature maps erzeugen.

![Beispiel Convolutional Layer mit einem Filter](.\Dateien\convLayer.png){width=50%}

### Pooling Layer

Ein weiterer Layer ist der Pooling Layer. Um die Dimensionen der Feature maps zu reduzieren werden pooling Layer verwendet. Dies reduziert den Rechenaufwand und somit die Zeit ein Netzwerk zu trainieren.

Ein Beispiel für einen pooling Layer ist max Pooling.

### Beispiel Max pooling

Bei diesem Beispiel ist die Feature map am Anfang eine 4x4 Matrix. Der Filter hat eine größe von 2x2 und wird immer um 2 Felder weiterbewegt. Für jede Region wird nur der maximale Wert übernommen und in eine neue Matrix eingetragen.

![Max pooling](.\Dateien\pooling.png){width=50%}

### Fully Connected Layer

Zum Schluss werden noch, wie bei einem Neuronalen Netzwerk, vollständig verbundene Layer verwendet um aus den Feature maps die endgültigen vorhersagen zu berechnen.

![Fully Connected Layer](.\Dateien\dense.png){width=40%}

## Umsetzung

Das Convolutional Neural Network wurde mit der open-source Library Tensorflow implementiert.


