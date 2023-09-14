import string

def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2): return False
    
    s1_freq_count = [0] * 26
    s2_freq_count = [0] * 26

    # initialise frequency counts
    for i in range(len(s1)):
        s1_freq_count[ord(s1[i]) - ord('a')] += 1
        s2_freq_count[ord(s2[i]) - ord('a')] += 1

    matches = 0
    for i in range(26):
        matches += 1 if s1_freq_count[i] == s2_freq_count[i] else 0

    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26: return True

        # slide window to the right if current window doesnt contain permutation
        index = ord(s2[r]) - ord('a')
        s2_freq_count[index] += 1
        if (s1_freq_count[index] == s2_freq_count[index]):
            matches += 1
        elif (s1_freq_count[index] + 1 == s2_freq_count[index]):
            matches -= 1

        index = ord(s2[l]) - ord('a')
        s2_freq_count[index] -= 1
        if (s1_freq_count[index] == s2_freq_count[index]):
            matches += 1
        elif (s1_freq_count[index] + 1 == s2_freq_count[index]):
            matches -= 1
        l += 1
    
    return False

print(checkInclusion("oabo", "eidbaooo"))
print(checkInclusion("dab", "eidbaooo"))