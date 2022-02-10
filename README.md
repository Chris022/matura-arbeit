# markdown-writer
Kann genutzt werden um wissenschaftliche arbeiten in Markdown zu schreiben.
For now only works on windows

### Requirements
Um dieses Tool zu nutzen muss
pandoc installiert werden: https://pandoc.org/installing.html
lualatex installiert werden: https://miktex.org/howto/install-miktex

### Wie man an dieser Arbeit schreibt
#### Ordnerstruktur
```
markdown-writer
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
