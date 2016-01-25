import os
import re
from shutil import copyfile
from subprocess import call


have_h1_inside = ['self', 'ruby-ecosystem', 'edn', 'zfs']
have_heading = ['asymptotic-notation']
dir_name = '_temp'
syntax_aliases = { # from github md to pandoc
	'coffeescript': ('coffeescript', 'coffee'),
	'common-lisp': ('common-lisp', 'commonlisp'),
	'csharp': ('csharp', 'cs'),
	'fsharp': ('csharp', 'fsharp'),
	'haxe': ('csharp', 'haxe'),
	'javascript': ('js', 'javascript'),
	'less': ('less', 'css'),
	'make': ('make', 'makefile'),
	'sass': ('scss', 'css'),
	'typescript': ('js', 'javascript'),
}

if not os.path.isdir(dir_name):
	os.mkdir(dir_name)

ls = []


for i in os.listdir():
	if os.path.isfile(i) and i.endswith('.html.markdown'):
		lang = i.replace('.html.markdown', '')
		if lang == 'latex' or lang == 'markdown':
			continue
		copyfile(i, dir_name + '/' + i)
		f = dir_name + '/' + i
		ls += [f]
		data = open(f, 'r', encoding='utf-8').read()
		data = re.sub(r'\-\-\-[\w\W]+?\-\-\-', '', data) # remove configs
		if lang in have_h1_inside:
			data = re.sub(r'\n# ', '\n## ', data)
		if lang not in have_heading:
			data = '# ' + lang.title() + '\n' + data
		if lang in syntax_aliases.keys():
			data = re.sub(r'\`\`\`.+', '```' + syntax_aliases[lang][1], data)
		open(f, 'w', encoding = 'utf-8').write(data)


call(
	['pandoc'] + 
	ls +
	['-o learnxinyminutes.pdf',
	'-V',
	'geometry:margin=1in',
	'--latex-engine=xelatex',
	# '--template=template.tex',
	]
	)