# Learn X in Y minutes - PDF

(**Updated** 27/8/16) [Learn X in Y minutes](http://learnxinyminutes.com) as PDF. Source = https://github.com/adambard/learnxinyminutes-docs


## Preview
![Screenshot](https://cloud.githubusercontent.com/assets/4047597/18028175/063ccd6a-6c95-11e6-9ebf-fba11c516afc.png)


## Download

* Downloads are hosted on [GitHub Releases](https://github.com/aviaryan/learnxinyminutes-pdf/releases/tag/v2016.08.27)
* [learnxinyminutes.pdf](https://github.com/aviaryan/learnxinyminutes-pdf/releases/download/v2016.08.27/learnxinyminutes.pdf) is the all-in-one PDF.
* The individual PDF files can be found as [release attachments](https://github.com/aviaryan/learnxinyminutes-pdf/releases/tag/v2016.08.27).
* If you want a zip of all individual PDF's, then download [learnxinyminutes_all.zip](https://github.com/aviaryan/learnxinyminutes-pdf/releases/download/v2016.08.27/learnxinyminutes_all.zip).


### Limitations

* `learnxinyminutes.pdf` doesn't include 2 languages; latex and markdown. This is because they caused conflicts while building the pdf (you can guess why). If needed, you can always download their individual pdf's from the [release attachments](https://github.com/aviaryan/learnxinyminutes-pdf/releases/tag/v2016.08.27).
 

### Building

1. Run `genpdf.py` (Python 3). It generates the all-in-one pdf and the parsed markdown files. 
2. Run `_genpdf.sh`. It generates the individual pdf-s. Note that this takes the generated files from Python script (in _temp directory) as the input.
3. To update on GitHub, first create a new release from the web UI. Then run `upload-releases.py`.

\* Requires `pandoc` and `latex` installed.
