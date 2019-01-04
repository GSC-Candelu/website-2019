#!/usr/bin/python
from jinja2 import Environment, FileSystemLoader


# jinja templates into html files conversion
SRC = './_src'
DIST = './_build'

IN_FILE_FORMAT= '_{}.html'
OUT_FILE_FORMAT= '{}/{}.html'

ENV = Environment(loader=FileSystemLoader(SRC))

YEAR = 2019
TITLE = 'Gruppo Sportivo & Culturale'
PAGES_LIST = ['home', 'sagra', 'vini', 'eventi', 'contatti',]   # order is the same as nav

PAGE_DATA = {
    'home': {'title': TITLE, }, 
    'sagra': {'title': 'Sagra | {}'.format(TITLE), },
    'vini': {'title': 'Mostra dei Vini | {}'.format(TITLE), 'aziende': 15},
    'eventi': {'title': 'Eventi | {}'.format(TITLE), 'eventi': ['borella', 'pedalata', 'motoconcentrazione']},
    'pitona': {'title': 'Pitona | {}'.format(TITLE), },
    'contatti': {'title': 'Contatti | {}'.format(TITLE), },
}

for item in PAGES_LIST:
    # fetch the template
    in_fname = IN_FILE_FORMAT.format(item)
    print('reading', in_fname)
    template = ENV.get_template(in_fname)

    # set some context and render the html
    ctx = PAGE_DATA[item]
    ctx.update({
        'year': YEAR,
        'enabled_pages': PAGES_LIST,
        'active_page': item,
    })
    print('data', ctx)
    html = template.render(ctx)

    # write the html in a file
    out_fname = OUT_FILE_FORMAT.format(DIST, item)
    print('writing', out_fname)
    with open(out_fname, 'w') as out_file:
        out_file.write(html)