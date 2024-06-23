def get_hash(pattern):
    return sum(ord(char) for char in pattern)
    #h = 0
    #for char in pattern:
    #    h = (h * 256 + ord(char)) % 101
    #return h


def RK_find(pattern, data):
    if pattern == "" or data == "" or len(pattern) > len(data):
        return None
    index_in_data = len(pattern)
    found_patterns_indices = []
    pattern_hash = get_hash(pattern)
    curr_hash = get_hash(data[0:index_in_data])
    if curr_hash == pattern_hash and data[0:index_in_data] == pattern:
        found_patterns_indices.append(0)
    while index_in_data < len(data):
        pattern_start = index_in_data - len(pattern) + 1
        curr_pattern = data[pattern_start:index_in_data + 1]
        #curr_hash = get_hash(data[pattern_start:index_in_data+1])
        curr_hash = curr_hash - get_hash(data[pattern_start - 1]) + get_hash(data[index_in_data])
        if (curr_hash == pattern_hash and curr_pattern == pattern):
            found_patterns_indices.append(pattern_start)
        index_in_data += 1
    return found_patterns_indices