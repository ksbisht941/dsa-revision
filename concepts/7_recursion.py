def power_set(items):
    """Return the power set (all subsets) of the input list using recursion."""
    if not items:
        return [[]]

    first, rest = items[0], items[1:]
    subsets_without_first = power_set(rest)
    subsets_with_first = [[first] + subset for subset in subsets_without_first]

    return subsets_without_first + subsets_with_first

items = [1, 2, 3]
print("Input:", items)
print("Power set:", power_set(items))