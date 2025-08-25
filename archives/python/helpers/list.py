def equal_ignore_order(a, b):
    """Use only when elements are neither hashable or sortable!"""
    unmatched = list(b)
    for element in a:
        try:
            unmatched.remove(element)
        except ValueError:
            return False
    return not unmatched
