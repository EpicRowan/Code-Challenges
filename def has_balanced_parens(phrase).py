def has_balanced_parens(phrase):
    """Does a string have balanced parentheses?"""
    counter = 0
    for char in phrase:
        if char == "(":
            counter += 1
        if char == ")":
            counter -= 1
    return True if counter == 0 else False
