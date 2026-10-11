import re

def fix_spaces(text):
    text = re.sub(r' {3,}', '-', text)
    return text.replace(' ', '_')