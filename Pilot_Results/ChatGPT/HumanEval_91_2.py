def is_bored(S):
    return sum(sentence.strip().startswith("I ") or sentence.strip() == "I"
               for sentence in __import__("re").split(r"[.!?]", S))