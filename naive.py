def naive_find(pattern, data):
    if pattern == "" or data == "" or len(pattern) > len(data):
        return None
    index_in_data = 0
    found_patterns_indices = []
    while index_in_data + len(pattern) - 1 < len(data):
        if data[index_in_data:index_in_data+len(pattern)] == pattern:
            found_patterns_indices.append(index_in_data)
        index_in_data += 1
    return found_patterns_indices