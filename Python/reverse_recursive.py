def reverse_str(s):
    if len(s) <= 1:
        return s[0]
    return reverse_str(s[1:]) + reverse_str(s[0])

