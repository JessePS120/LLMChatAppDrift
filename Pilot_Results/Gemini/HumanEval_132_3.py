def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    stack = []
    pairs = []
    for i, char in enumerate(string):
        if char == '[':
            stack.append(i)
        elif char == ']' and stack:
            start = stack.pop()
            pairs.append((start, i))
    
    for s1, e1 in pairs:
        for s2, e2 in pairs:
            if s2 < s1 and e1 < e2:
                return True
    return False