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
    opening = [i for i, c in enumerate(string) if c == '[']
    closing = [i for i, c in enumerate(string) if c == ']']
    closing.reverse()

    count = 0
    j = 0
    for idx in opening:
        if j < len(closing) and idx < closing[j]:
            count += 1
            j += 1
    return count >= 2