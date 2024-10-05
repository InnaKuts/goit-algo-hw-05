def binary_search(lst: list[float], target: float):
    left, right = 0, len(lst) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (right + left) // 2

        if lst[mid] == target:
            return iterations, lst[mid]

        if lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if left < len(lst):
        upper_bound = lst[left]

    return iterations, upper_bound


print(binary_search([1.1, 2.5, 3.3, 4.8, 5.5, 6.7], 0))
print(binary_search([1.1, 2.5, 3.3, 4.8, 5.5, 6.7], 1.1))
print(binary_search([1.1, 2.5, 3.3, 4.8, 5.5, 6.7], 3))
print(binary_search([1.1, 2.5, 3.3, 4.8, 5.5, 6.7], 5))
print(binary_search([1.1, 2.5, 3.3, 4.8, 5.5, 6.7], 7))
