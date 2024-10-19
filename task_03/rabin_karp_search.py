def polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def rabin_karp_search(string: str, substr: str):
    substring_length = len(substr)
    main_string_length = len(string)

    base = 256
    modulus = 101

    substring_hash = polynomial_hash(substr, base, modulus)
    current_slice_hash = polynomial_hash(string[:substring_length], base, modulus)

    h_multiplier = pow(base, substring_length - 1) % modulus

    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if string[i:i + substring_length] == substr:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1
