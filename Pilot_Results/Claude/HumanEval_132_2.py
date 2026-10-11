def is_nested(string):
    opening_idx = []
    closing_idx = []
    for i, c in enumerate(string):
        if c == '[':
            opening_idx.append(i)
        elif c == ']':
            closing_idx.append(i)
    closing_idx.reverse()
    cnt = 0
    j = 0
    for idx in opening_idx:
        if j < len(closing_idx) and idx < closing_idx[j]:
            cnt += 1
            j += 1
    return cnt >= 2