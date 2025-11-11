def change_case(strings, to_upper=False):
    return ' '.join(s.upper() if to_upper else s.lower() for s in strings)

def filter_combined_lists(list1, list2, filter_function=None):
    combined = list1 + list2
    return combined if filter_function is None else list(filter(filter_function, combined))

def unique_sorted_numbers(numbers):
    return sorted(set(numbers))

def strings_starting_with_upper(*args):
    return [s for s in args if s and s[0].isupper()]
