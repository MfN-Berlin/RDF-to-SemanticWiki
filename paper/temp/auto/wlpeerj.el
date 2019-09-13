(TeX-add-style-hook
 "wlpeerj"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("babel" "english") ("geometry" "left=5cm" "right=2cm" "top=2.25cm" "bottom=2.25cm" "headheight=12pt" "letterpaper") ("caption" "labelfont={bf,sf}" "labelsep=period" "justification=raggedright") ("titlesec" "explicit")))
   (TeX-run-style-hooks
    "latex2e"
    "inputenc"
    "babel"
    "ifthen"
    "calc"
    "microtype"
    "article"
    "art10"
    "times"
    "mathptmx"
    "lineno"
    "ifpdf"
    "amsmath"
    "amsfonts"
    "amssymb"
    "graphicx"
    "xcolor"
    "booktabs"
    "authblk"
    "geometry"
    "caption"
    "natbib"
    "fancyhdr"
    "lastpage"
    "titlesec"
    "titletoc"
    "enumitem"
    "lipsum")
   (TeX-add-symbols
    '("corrauthor" ["argument"] 2)
    '("keywords" 1)
    "wllogo"
    "keywordname"
    "thecorrauthor"
    "xabstract"
    "abstract"
    "two"
    "go"
    "oldbibliography")
   (LaTeX-add-lengths
    "tocsep"))
 :latex)

