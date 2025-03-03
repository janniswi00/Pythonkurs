def PatternCount(text:str, pattern:str):
    count = 0
    for i in range(len(text) - len(pattern) +1):
        if text[i: i+len(pattern)] == pattern:
            count += 1
    return count

def FrequentWords_slow(text, k):
    frequent_patterns = []
    counts = []

    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        counts.append(PatternCount(text, pattern))
    
    max_count = max(counts)

    for i in range(len(text) - k +1):
        if counts[i] == max_count:
            frequent_patterns.append(text[i:i+k])
    
    return set(frequent_patterns), max_count

def FrequencyTable(text, k):
    freq_map = {}
    n = len(text)

    for i in range(n-k+1):
        pattern = text[i:i+k]
        if pattern not in freq_map.keys():
            freq_map[pattern] = 1
        else:
            freq_map[pattern] += 1
    
    return freq_map

def BetterFrequentWords(text, k):
    frequent_patterns = []
    freq_map = FrequencyTable(text, k)
    maximum = max(freq_map.values())

    for pattern in freq_map.keys():
        if freq_map[pattern] == maximum:
            frequent_patterns.append(pattern)
    return frequent_patterns, maximum

def GetReverse(sequence:str):
    return sequence.translate(str.maketrans("ACGTacgt","TGCAtgca"))[::-1]


def PatternMatching(genome, pattern):
    starting_positions = []
    for i in range(len(genome)-len(pattern) +1):
        if pattern == genome[i:i+len(pattern)]:
            starting_positions.append(i)
    return starting_positions

def FindClumps(text:str, k:int, L:int, t:int) ->list:
    """_summary_

    Args:
        text (str): DNA-Sequence
        k (int): k-mers
        L (int): length of window
        t (int): number of same sequence in window
    """
    patterns = []
    n = len(text)

    for i in range(n-L+1):
        window = text[i:i+L]
        freq_map = FrequencyTable(window, k)

        for key in freq_map.keys():
            if freq_map[key] >= t:
                patterns.append(key)
    return(list(set(patterns)))
