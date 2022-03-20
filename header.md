---
author: <author-placeholder>
title: <title-placeholder>
geometry: margin=1in
fontfamily: Cabin
fontfamilyoptions: sfdefault
numbersections: true
toc-title: Inhalt
header-includes: |
    \usepackage{graphicx}
    \usepackage{fancyhdr}
    \graphicspath{ {figures/} }
    \pagestyle{fancy}
    \setlength\headheight{20pt}
    \rhead{Doc generator}
    \usepackage{float}
    \floatplacement{figure}{H}
    \floatplacement{table}{H}
    \renewcommand{\listfigurename}{}
    \lstset{frame = single}
    \renewcommand{\figurename}{Abbildung}
    \renewcommand*\contentsname{}
---
\newpage
# Inhaltsverzeichnis
\tableofcontents
\newpage