def N(pattern, text):
    if pattern == "" or text == "" or len(pattern) > len(text):
        return None
    pattern_length = len(pattern)
    text_length = len(text)
    matches = []
    for i in range(text_length - pattern_length + 1):
        match = True
        for j in range(pattern_length):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            matches.append(i)
    return matches