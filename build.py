#!/usr/bin/python
from jinja2 import Environment, FileSystemLoader


# Converts Jinja templates into HTML files.


ENV = Environment(loader=FileSystemLoader('./_src'))

# List of pages to be rendered -- MUST be listed according to their
# order in the navigation bar
PAGE_LIST = ['home', 'sagra', 'vini', 'eventi', 'pitona', 'contatti',]

# Title of individual pages
TITLES = {
    'home': 'Gruppo Sportivo & Culturale',
    'sagra': 'Gruppo Sportivo & Culturale | Sagra',
    'vini': 'Gruppo Sportivo & Culturale | Mostra dei Vini',
    'eventi': 'Gruppo Sportivo & Culturale | Eventi',
    'pitona': 'Gruppo Sportivo & Culturale | Pitona',
    'contatti': 'Gruppo Sportivo & Culturale | Contatti',
}
YEAR = 2019

for item in PAGE_LIST:
    file_name = item + '.html'
    template = ENV.get_template(file_name)
    html = template.render(title=TITLES[item], year=YEAR)

    # Write output in the corresponding HTML file
    print 'Writing', file_name
    with open(file_name, 'w') as out_file:
        out_file.write(html)