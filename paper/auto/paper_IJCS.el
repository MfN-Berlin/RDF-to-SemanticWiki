(TeX-add-style-hook
 "paper_IJCS"
 (lambda ()
   (TeX-run-style-hooks
    "latex2e"
    "ijcs_template"
    "ijcs_template10")
   (LaTeX-add-labels
    "tab1")
   (LaTeX-add-bibitems
    "berners1998"
    "corcho2003"
    "diiorio2006"
    "gandon2014"
    "kiniti2013"
    "musen2015"
    "noy2001"
    "oren2006"
    "ortiz2016"
    "patzschke2016"
    "pieterse2014"
    "zhou2007"))
 :latex)

