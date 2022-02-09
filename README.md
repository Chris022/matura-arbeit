# matura-arbeit
Matura Arbeit

### Wie man an dieser Arbeit schreibt
#### Ordnerstruktur
```
matura-arbeit
│   README.md
│   compiler.py
│   config.json
│   out.pdf      ---- automatisch generiert!
│
└───Kapitel
    │
    └───Kapitel_1
        │   text.md
        │
        └───Daten
                Bild1.png
                ...
```
#### Vorgehensweise
Jedes Kapitel wird in einem eigenen Branch geschrieben und wird nach Vervollständigung auf dev gemerged
Jeder Release wird auf Main gemerged
Für jedes Kapitel erstellt man einen eigenen Ordner

### Compile
Zum generieren des pdfs muss lediglich der compiler.py ausgeführt werden