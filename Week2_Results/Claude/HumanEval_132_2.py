def is_nested(string):
    for i in range(len(string)):
        if string[i] == '[':
            opens = 1
            closes = 0
            for j in range(i + 1, len(string)):
                if string[j] == '[':
                    opens += 1
                elif string[j] == ']':
                    closes += 1
                
                if opens == closes and opens > 1:
                    return True
    
    return False