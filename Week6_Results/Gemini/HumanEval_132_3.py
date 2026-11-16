def is_nested(string):
    opens = [i for i, c in enumerate(string) if c == '[']
    closes = [i for i, c in enumerate(string) if c == ']']
    if len(opens) < 2 or len(closes) < 2:
        return False
    valid_closes = [c for c in closes if c > opens[1]]
    return len(valid_closes) >= 2