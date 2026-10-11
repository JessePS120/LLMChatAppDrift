import re


def is_bored(S):
    sentences = re.split(r"[.?!]", S)
    count = 0
    for s in sentences:
        words = s.strip().split()
        if words and words[0] == "I":
            count += 1
    return count