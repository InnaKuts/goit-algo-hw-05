
def build_shift_table(substr: str):
    table = {}
    length = len(substr)
    for index, char in enumerate(substr[:-1]):
        table[char] = length - index - 1
    table.setdefault(substr[-1], length)
    return table


def boyer_moore_search(string: str, substr: str):
    shift_table = build_shift_table(substr)
    i = 0

    while i <= len(string) - len(substr):
        j = len(substr) - 1

        while j >= 0 and string[i + j] == substr[j]:
            j -= 1

        if j < 0:
            return i

        i += shift_table.get(string[i + len(substr) - 1], len(substr))

    return -1
