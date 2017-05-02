def compare_digest(val1, val2):
    if len(val1) != len(val2): return False
    result = 0
    for i, j in zip(val1, val2):
      result |= (ord(i) ^ ord(j))
    return result == 0