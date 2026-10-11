def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    """
    import re
    sentences = re.split(r'[.?!]', S)
    return sum(1 for sentence in sentences if sentence.strip().startswith('I') and
               (len(sentence.strip()) == 1 or sentence.strip()[1].isspace()))