def is_nested(string):
    opens = [i for i, c in enumerate(string) if c == '[']
    closes = [i for i, c in enumerate(string) if c == ']']
    for i2 in opens:
        for j2 in closes:
            if i2 < j2 and any(i < i2 for i in opens) and any(j > j2 for j in closes):
                return True
    return False