def biggest(numbers):
    best = numbers[0]
    for n in numbers:
        if n > best:
            best = n
    return best
print(biggest([4,9,2,7,5,1,3,8,6]))