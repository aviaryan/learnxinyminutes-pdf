#!/usr/bin/env python3

"""Script to generate a synoptic .pdf about the entries of learnxinyminutes.

For proper execution, this script depends on a working installation of
+ Python (e.g., https://www.python.org/)
+ Pandoc (e.g., https://pandoc.org/)
+ XeLaTeX (e.g., https://en.wikipedia.org/wiki/XeTeX)

Copy the markdown files of your interest into this project's folder, and
run

python genpdf.py

to build file learnxinyminutes.pdf."""

import os
import re
from shutil import copyfile
from subprocess import call

##############
# BUILD CONFIGS
##############

# Have H1 headings inside. They come as root in TOC when pdf is generated.
have_h1_inside = [
    'self', 'ruby-ecosystem', 'edn', 'zfs', 'dynamic-programming',
    'binary-search', 'php-composer'
]

# Have the main heading in *.md. So adding a custom heading is not needed.
have_heading = ['asymptotic-notation']

# Directory to store temporary md files
DIR_NAME = '_temp'

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
if not os.path.isdir(DIR_NAME):
    os.mkdir(DIR_NAME)

ls = []

for i in os.listdir():
    if os.path.isfile(i) and i.endswith('.html.markdown'):
        lang = i.replace('.html.markdown', '')
        # copy the files . also used by _genpdf.sh
        copyfile(i, DIR_NAME + '/' + i)
        # Don't build them as they create problems
        if lang in ['latex', 'markdown']:
            continue
        f = DIR_NAME + '/' + i
        ls += [f]

        # Process file
        try:
            with open(f, mode='r', encoding='utf-8') as source:
                data = source.read()
        except OSError:
            print(f"Error reading from file {f}.")

        # remove configs
        data = re.sub(r'\-\-\-[\w\W]+?\-\-\-', '', data, count=1)
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
        try:
            with open(f, mode='w', encoding='utf-8') as newfile:
                newfile.write(data)
        except OSError:
            print(f"Error writing into file {f}.")

ls = sorted(ls)

call(['pandoc'] + ls + [
    '-o',
    'learnxinyminutes.pdf',
    '-V',
    'geometry:margin=1in',
    '--pdf-engine=xelatex',
    # '--template=template.tex',
])
