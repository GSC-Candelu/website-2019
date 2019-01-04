from datetime import datetime


YEAR = datetime.today().year
# this is when it all usually starts, so we still show last year's assets
# until the time comes to update them with the new ones
# TODO: replace check against the start date rather than just checking the month
if datetime.today().month <= 4:
    YEAR = YEAR - 1

START_DATE = ''
END_DATE = ''

TITLE = 'Gruppo Sportivo & Culturale'
PAGES_LIST = ['home', 'sagra', 'vini', 'eventi', 'contatti',]   # order is the same as nav

def get_context():
    # create common context for all pages
    ctx = {
        'year': YEAR,
        'start_date': START_DATE,
        'end_date': END_DATE,
        'enabled_pages': PAGES_LIST,
    }
    return ctx

# page specific context
PAGE_DATA = {
    'home': {
        'title': TITLE,
        'active_page': 'home',
    },

    'sagra': {
        'title': 'Sagra | {}'.format(TITLE),
        'active_page': 'sagra',
    },

    'vini': {
        'title': 'Mostra dei Vini | {}'.format(TITLE),
        'active_page': 'vini',
        'aziende': 15,
    },

    'eventi': {
        'title': 'Eventi | {}'.format(TITLE),
        'active_page': 'eventi',
        'eventi': ['borella', 'pedalata', 'motoconcentrazione']
    },

    'pitona': {
        'title': 'Pitona | {}'.format(TITLE),
        'active_page': 'pitona',
    },

    'contatti': {
        'title': 'Contatti | {}'.format(TITLE),
        'active_page': 'contatti',
    },
}