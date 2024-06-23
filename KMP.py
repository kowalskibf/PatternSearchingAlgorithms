def get_prefix(pattern):
    j = 0
    i = 1
    prefix = len(pattern)*[0]
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            prefix[i] = j+1
            j += 1
            i += 1
        else:
            if j != 0:
                j = prefix[j-1]
            else:
                i += 1
    return prefix


def KMP_find(pattern, data):
    if pattern == "" or data == "" or len(pattern) > len(data):
        return None
    index_pattern = 0
    index_in_data = 0
    found_patterns_indices = []
    prefix = get_prefix(pattern)
    while index_in_data < len(data):
        if pattern[index_pattern] == data[index_in_data]:
            index_pattern += 1
            index_in_data += 1
            if index_pattern == len(pattern):
                found_patterns_indices.append(index_in_data - index_pattern)
                index_pattern = prefix[index_pattern - 1]
        else:
            if index_pattern != 0:
                index_pattern = prefix[index_pattern - 1]
            else:
                index_in_data += 1
    return found_patterns_indices

