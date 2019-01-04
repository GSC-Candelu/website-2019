#!/usr/bin/python
import site_data

from jinja2 import Environment, FileSystemLoader


# jinja templates into html files conversion
SRC = './_src'
DIST = './_build'
IN_FILE_FORMAT= '_{}.html'
OUT_FILE_FORMAT= '{}/{}.html'
ENV = Environment(loader=FileSystemLoader(SRC))


def build_html(page):
    # fetch the template
    in_fname = IN_FILE_FORMAT.format(page)
    print('reading', in_fname)
    template = ENV.get_template(in_fname)

    # set some context and render the html
    ctx = site_data.get_context()  # get common context
    ctx.update(site_data.PAGE_DATA[page])  # get page specific context

    print('data', ctx)
    html = template.render(ctx)

    return html

for page in site_data.PAGES_LIST:
    # create the html output for a page
    html = build_html(page)

    # write the html in a file
    out_fname = OUT_FILE_FORMAT.format(DIST, page)
    print('writing', out_fname)
    with open(out_fname, 'w') as out_file:
        out_file.write(html)