---
geometry: margin=1in
mainfont: Calibri
numbersections: true
header-includes: |
    \usepackage{fontspec}
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

    \fancyfoot[R]{HTBLuVA - Elektronik}
    \fancyhead[R]{2021/22}
    \fancyhead[C]{Smarter Circuits}
    \fancyhead[L]{Diplomarbeit}

    \title{<title-placeholder>}
    \author{<author-placeholder>}
---
\maketitle
\newpage