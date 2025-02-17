def PatternCount(text:str, pattern:str):
    count = 0
    for i in range(len(text) - len(pattern)):
        if text[i: i+len(pattern)] == pattern:
            count += 1
    return count

def FrequentWords_slow(text, k):
    frequent_patterns = []
    counts = []

    for i in range(len(text) - k):
        pattern = text[i:i+k]
        counts.append(PatternCount(text, pattern))
    
    max_count = max(counts)

    for i in range(len(text) - k):
        if counts[i] == max_count:
            frequent_patterns.append(text[i:i+k])
    
    return frequent_patterns, max_count

def FrequencyTable(text, k):
    freq_map = {}
    n = len(text)

    for i in range(n-k):
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

def GetReverse(sequence):
    reverse_genome = ""
    for i in range(len(sequence)):
        complementary_base = None
        if sequence[i] == "A":
            complementary_base = "T"
        elif sequence[i] == "T":
            complementary_base = "A"
        elif sequence[i] == "G":
            complementary_base = "C"
        elif sequence[i] == "C":
            complementary_base = "G"
        reverse_genome += complementary_base
    return reverse_genome

def PatternMatching(genome, pattern):
    starting_positions = []
    for i in range(len(genome)-len(pattern)):
        if pattern == genome[i:i+len(pattern)]:
            starting_positions.append(i)
    return starting_positions