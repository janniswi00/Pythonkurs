def PatternCount(text:str, pattern:str):
    count = 0
    for i in range(len(text) - len(pattern)):
        if text[i: i+len(pattern)] == pattern:
            count += 1
    return count