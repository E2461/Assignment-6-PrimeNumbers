numbers = []
prime_numbers = []
i = 1
while i < 101:
    numbers.append(i)
    i+=1
#print(numbers)
counter = 0

for x in numbers:
    for y in numbers:
        if x % y == 0:
            counter+=1
    if counter == 2:
        prime_numbers.append(x)
    counter = 0
print(prime_numbers)
