mkdir _pdfs;
#pandoc coffeescript.html.markdown -s -o _pdfs/coffeescript.pdf -V geometry:margin=1in --latex-engine=xelatex;
#exit 1;
for file in _temp/*.html.markdown
do
	base=$(basename $file);
	langname=${base//\.html\.markdown/};
	echo "Making PDF $langname";
	pandoc $file -s -o _pdfs/$langname.pdf -V geometry:margin=1in --latex-engine=xelatex
done

mv _pdfs/c++.pdf _pdfs/cpp.pdf;