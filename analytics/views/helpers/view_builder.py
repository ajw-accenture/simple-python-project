HTML_PREFIX = '<html><head></head><body>'
HTML_POSTFIX = '</body></html>'

def build_full_page(content):
    return f'{HTML_PREFIX}{content}{HTML_POSTFIX}'
