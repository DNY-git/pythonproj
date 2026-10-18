def average(numbers):
    total = 0
    for n  in numbers:
        total = total + n
    return total / len(numbers)
scores = [85, 92, 78, 96, 88]
print(average(scores))