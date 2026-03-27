def isSameNumber(numbers):
    for number in numbers:
        num = numbers[0]
        if num != number:
            return False
    return True
        
print(isSameNumber([1, 2, 1, 1, 1]))