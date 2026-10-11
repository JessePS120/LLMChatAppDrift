import re

def is_bored(S):
    sentences = re.split(r'[.?!]', S)
    count = 0
    for sentence in sentences:
        words = sentence.strip().split()
        if words and words[0] == "I":
            count += 1
    return count