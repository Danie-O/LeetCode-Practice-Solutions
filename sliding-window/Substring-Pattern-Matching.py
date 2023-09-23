def findPattern(text: str, pattern: str):
    text_length = len(text)
    pattern_length = len(pattern)

    # we cannot find empty pattern in non-empty text, or non-empty pattern in empty text
    if not text_length or not pattern_length: return -1

    for i in range(text_length - pattern_length):
        j = 0

        while (j < pattern_length) and (text[i + j] == pattern[j]):
            j += 1
        # we have found pattern if the below is true, so we return the start of window
        if j == pattern_length:
            return i

    return -1 # if we dont find pattern in input text

print(findPattern("Daniella", "an"))    # result = index 1
print(findPattern("Daniella", "e"))    # result = index 4
print(findPattern("Daniella", "ang"))   # result = index -1 (pattern not found)