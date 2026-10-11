import re

def fix_spaces(text):
    text = re.sub(r' {3,}', '-', text)
    text = text.replace(' ', '_')
    return text