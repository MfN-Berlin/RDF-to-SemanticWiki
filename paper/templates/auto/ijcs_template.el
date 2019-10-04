(TeX-add-style-hook
 "ijcs_template"
 (lambda ()
   (TeX-run-style-hooks
    "latex2e"
    "ijcs_template10")
   (LaTeX-add-labels
    "eq:jaa"
    "theo1"
    "lemma1"
    "one"
    "tab1"
    "a1")
   (LaTeX-add-bibitems
    "braley"
    "chhikara"
    "gupta95a"
    "gupta95b"
    "gupta97"
    "gurland94"
    "gurland95"
    "jorgensen"
    "mills71"
    "park99"
    "tang"
    "winkler"
    "wong88"
    "wong89"
    "wong91"))
 :latex)

