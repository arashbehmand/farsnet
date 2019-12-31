def _java_string_hashcode(s):
    s = s.encode("utf8").decode('utf8')
    h = 0
    for c in s:
        h = int((((31 * h + ord(c)) ^ 0x80000000) & 0xFFFFFFFF) - 0x80000000)
    return h