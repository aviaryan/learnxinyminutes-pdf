# Learn X in Y minutes - PDF

Built from https://github.com/adambard/learnxinyminutes-docs

![Screenshot](screenshot.png)


## Download

* [learnxinyminutes.pdf](https://github.com/aviaryan/learnxinyminutes-pdf/raw/master/learnxinyminutes.pdf) is the all-in-one pdf.
* The individual pdf files are present inside the [_pdfs](_pdfs) directory.


### Limitations

* learnxinyminutes.pdf doesn't include 2 languages; latex and markdown. This is because they caused conflicts while building the pdf (you can guess why). If needed, you can always download their individual pdf's from the [_pdfs](_pdfs) folder.
 

## Building

* `genpdf.py` generates the all-in-one pdf . It is written in Python 3.
* `_genpdf.sh` generates individual pdfs.
* Require `pandoc` and `latex`.