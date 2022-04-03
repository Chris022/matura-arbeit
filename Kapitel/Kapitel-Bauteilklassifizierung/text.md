# Bauteilklassifizierung

## Problem

Um die Schaltung zu digitalisieren, müssen alle Bauteile, nachdem deren Position gefunden worden ist, noch richtig erkannt werden.

Die zuvor gesuchten Muster in dem Graphen der Schaltung reichen jedoch nicht aus, um jedes Bauteil zu bestimmen, da zum Beispiel ein Widerstand und eine Spule dasselbe Muster haben.

## Idee

Um die Bauteile zu erkennen, soll ein "Convolutional Neural Network" verwendet werden.

![Funktion CNN](.\Dateien\cnn.png){width=70%}

Diesem Netzwerk wird das Bild eines Bauteiles übergeben und als Antwort erhält man, um welches Bauteil es sich am wahrscheinlichsten handelt.

## Neuronales Netzwerk

Ein Neuronales Netzwerk ist ein Algorithmus, der dem menschlichen Gehirn nachempfunden ist. Solche Netzwerke können verwendet werden, um Muster in Daten zu finden, wie zum Beispiel Gegenstände auf Bildern zu erkennen.

### Aufbau

Ein Neuronales Netzwerk besteht aus Neuronen, die in mehreren Schichten (Layer) angeordnet sind. Jedes Netzwerk hat am Anfang einen Input Layer sowie am Ende einen Output Layer. Zwischen diesen beiden Layers können einer oder mehrere Hidden Layer liegen.

![Struktur eines Neuronalen Netzwerkes](.\Dateien\aufbauNN.png){width=70%}

Jedes Neuron enthält eine Nummer, auch Aktivierung genannt.

Um Bauteile einer Schaltung zu erkennen, würde die Aktivierung der Neuronen im Input Layer jeweils der Pixelwert eines Bildes sein.

![Input Layer eines Neuronalen Netzwerkes](.\Dateien\inputLayer.png){width=70%}

Die Größe des Output Layer wäre die Anzahl der verschiedenen Bauteile, die dieses Netzwerk erkennen kann. Dabei entspricht die Aktivierung eines Neurons am Ausgang der Wahrscheinlichkeit, dass auf dem Bild das jeweilige Bauteil abgebildet ist. 

![Output Layer eines Neuronalen Netzwerkes](.\Dateien\outputLayer.png){width=70%}

\newpage

Alle Neuronen in einem Layer sind mit jeweils allen Neuronen aus dem vorherigen Layer verbunden. Jede dieser Verbindungen ist jedoch unterschiedlich gewichtet und beeinflusst somit das Neuron unterschiedlich stark. Diese Gewichtungen werden "weights" genannt.
Zusätzlich besitzt jedes Neuron noch einen Schwellwert (bias).

Um die Aktivierung eines Neurons zu ermitteln, wird zuerst die gewichtete Summe berechnet. Für die gewichtete Summe z wird jeder Eingang x mit seinem jeweiligen Gewicht w multipliziert und diese werden zum bias des Neurons addiert. Die gewichtete Summe wird zum Schluss einer Funktion (Activation function) übergeben, der Funktionswert entspricht der Aktivierung.

![Aktivierung eines Neurons](.\Dateien\singleNeuron.png){width=70%}

In einem Neuronalen Netzwerk sind die Eingänge x jeweils die Aktivierung aus dem vorherigen Layer.

![Berechnung der Aktivierung in einem Netzwerk](.\Dateien\calculate.png){width=70%}

### Trainieren eines Neuronalen Netzwerkes

Die Gewichte und Schwellwerte eines Neuronalen Netzwerkes können "erlernt" werden.
Das dafür genutzte Verfahren wird "Backpropagation" genannt.
Um ein Netzwerk zu trainieren wird eine große Anzahl an Trainingsdaten benötigt. Das sind Daten, bei denen der gewünschte Ausgabewert bereits bekannt ist. 

\newpage

### Funktionsweise Backpropagation

Zuerst werden die Gewichte und Schwellwerte zufällig gewählt. Danach wird die Ausgabe des Netzwerkes für ein Trainingsbild mit dem gewünschten Ausgabewert verglichen und es kann somit festgestellt werden, wie gut das Netzwerk fuktioniert. 
Die Differenz des gewünschten Ausgabewertes und des tatsächlichen Ausgabewertes sind der Fehler des Netzwerkes.

Daraufhin werden die Gewichte und Schwellwerte des Netzwerkes, beginnend vom Output Layer, so verändert, dass die Ausgabe des Netzwerkes sich dem gewünschten Ausgabewert annähert. 

Dies wird für alle Trainingsdaten so lange wiederholt, bis die Ausgabe des Netzwerkes mit den gewünschten Ausgabewerten annähernd übereinstimmt.

## Convolutional Neural Network

Ein Convolutional Neural Network besitzt im Gegensatz zu einem Neuronalen Netzwerk mehr verschiedene Layer, welche sich besser eignen um Informationen aus einem Bild zu extrahieren.


### Filter

Bei einem Convolutional Layer werden ein oder mehrere Filter verwendet.
Ein Filter ist dabei ein einfacher zweidimensionaler Array.
Diese Filter werden dabei über das Bild geschoben und die darunter liegenden Werte werden mit den Filterwerten multipliziert und addiert. Der resultierende Wert wird daraufhin in einer sogennanten "Feature map" gespeichert.

### Beispiel Filter

Bei diesem Beispiel wird ein Filter verwendet, um eine spezielle Ecke zu erkennen. Je höher der Wert in der Feature map, desto höher ist die Übereinstimmung. 

![Beispiel Filter zur Erkennung von Ecken](.\Dateien\filter.png){width=70%}

\newpage

### Convolutional Layer

Ein Convolutional Layer besteht meist aus mehreren Filtern, die eine Vielzahl an Feature maps erzeugen.

![Beispiel Convolutional Layer mit einem Filter](.\Dateien\convLayer.png){width=50%}

### Pooling Layer

Ein weiterer Layer ist der Pooling Layer. Um die Größe der Feature maps zu reduzieren, werden Pooling Layer verwendet. 
Dadurch besitzt das Netzwerk weniger Parameter die erlernt werden müssen, wodurch der Rechenaufwand und somit die Zeit um ein Netzwerk zu trainieren reduziert wird.

Ein Beispiel für einen Pooling Layer ist Max Pooling.

### Beispiel Max pooling

Bei diesem Beispiel ist die Feature map am Anfang eine 4x4 Matrix. Der Filter hat eine Größe von 2x2 und wird immer um zwei Felder weiterbewegt. Für jede Region wird nur der maximale Wert übernommen und in eine neue Matrix eingetragen.

![Max pooling](.\Dateien\pooling.png){width=50%}

\newpage

### Fully Connected Layer

Zum Schluss werden noch, wie bei einem Neuronalen Netzwerk, vollständig verbundene Layer verwendet, um aus den Feature maps die endgültigen Vorhersagen zu berechnen.

![Fully Connected Layer](.\Dateien\dense.png){width=40%}

## Umsetzung

Das Convolutional Neural Network wurde mit der Open Source Library Tensorflow implementiert.

Die Position der Bauteile ist bereits bekannt. Die davor erstellten Bounding Boxen werden aus dem Binärbild ausgeschnitten und auf eine Größe von 32x32 Pixel skaliert. Durch das Skalieren des Bildausschnittes ergeben sich für einzelne Pixel auch andere Werte wie 0 oder 255, es handelt sich daher um ein Graustufenbild und kein Binärbild. Die einzelnen Pixelwerte des Bildausschnittes werden davor noch durch 255 dividiert, damit jeder Wert zwischen 0 und 1 liegt. Jedes davor gefundene Bauteil wird so mithilfe des Convolutional Neural Networks klassifiziert.

![Fully Connected Layer](.\Dateien\box.png){width=70%}

