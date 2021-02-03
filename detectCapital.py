def detectCapital(s):
    if s.isupper():
        return True
    if s.islower():
        return True
    if s[0].isupper and s[1:].islower():
        return True
    return False
