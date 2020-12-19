(TeX-add-style-hook
 "paper"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("acmart" "manuscript" "screen" "review")))
   (TeX-run-style-hooks
    "latex2e"
    "acmart"
    "acmart10")
   (TeX-add-symbols
    "BibTeX")
   (LaTeX-add-labels
    "tab1")
   (LaTeX-add-bibliographies
    "paper.bib"))
 :latex)

