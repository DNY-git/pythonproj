def smallest(numbers):
    best = numbers[0]
    for n in numbers:
        if n < best:
            best = n
    return best
print(smallest([3, 8, 5, 10, 1]))