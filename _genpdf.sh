mkdir _pdfs;
for file in *.html.markdown
do
	langname=${file//\.html\.markdown/};
	echo "Making PDF $langname";
	pandoc $file -s -o _pdfs/$langname.pdf -V geometry:margin=1in --latex-engine=xelatex
done