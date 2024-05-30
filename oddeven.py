numbers = [12, 24, 35, 25, 99, 45, 38]
odd = []
even = []
while len(numbers) > 0:
    number = numbers.pop()
    if (number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)
print("Even numbers:", even)
print("Odd numbers:", odd)