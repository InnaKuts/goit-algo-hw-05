def compute_lps(substr: str):
    lps = [0] * len(substr)
    length = 0
    i = 1

    while i < len(substr):
        if substr[i] == substr[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(string: str, substr: str):
    M = len(substr)
    N = len(string)

    lps = compute_lps(substr)

    i = j = 0

    while i < N:
        if substr[j] == string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1  # якщо підрядок не знайдено
