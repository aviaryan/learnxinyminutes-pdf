import os
import re
from shutil import copyfile
from subprocess import call


##############
# BUILD CONFIGS
##############

# Have H1 headings inside. They come as root in TOC when pdf is generated.
have_h1_inside = ['self', 'ruby-ecosystem', 'edn', 'zfs', 'dynamic-programming', 'binary-search', 'php-composer']

# Have the main heading in *.md. So adding a custom heading is not needed.
have_heading = ['asymptotic-notation']

# Directory to store temporary md files
dir_name = '_temp'

# Syntax keyword conversions from Github markdown to Pandoc
syntax_aliases = {
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

# Create md directory if not exists
if not os.path.isdir(dir_name):
	os.mkdir(dir_name)

ls = []


for i in os.listdir():
	if os.path.isfile(i) and i.endswith('.html.markdown'):
		lang = i.replace('.html.markdown', '')
		# copy the files . also used by _genpdf.sh
		copyfile(i, dir_name + '/' + i)
		# Don't build them as they create problems
		if lang == 'latex' or lang == 'markdown':
			continue
		f = dir_name + '/' + i
		ls += [f]
		# Process file
		data = open(f, 'r', encoding='utf-8').read()
		# remove configs
		data = re.sub(r'\-\-\-[\w\W]+?\-\-\-', '', data, count = 1)
		# remove h1 headings in md file
		if lang in have_h1_inside:
			data = re.sub(r'\n# ', '\n## ', data)
		# add custom heading if main h1 heading not exists
		if lang not in have_heading:
			data = '# ' + lang.title() + '\n' + data
		# convert syntax keyword to pandoc
		if lang in syntax_aliases.keys():
			data = re.sub(r'\`\`\`.+', '```' + syntax_aliases[lang][1], data)
		# Save file
		open(f, 'w', encoding = 'utf-8').write(data)


ls = sorted(ls)

call(
	[
		'pandoc'
	] + 
	ls +
	[
		'-o',
		'learnxinyminutes.pdf',
		'-V',
		'geometry:margin=1in',
		'--latex-engine=xelatex',
		# '--template=template.tex',
	]
)
