# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Используя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
# Выведите списки primes и not_primes на экран(в консоль).

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(len(numbers) - 1):
    if numbers[i] < 2:
        continue
    for j in range(2, numbers[i] + 1):
        if (numbers[i] % j) == 0 and numbers[i] != j:
            not_primes.append(numbers[i])
            break
        if j == numbers[i]:
            primes.append(numbers[i])
print(primes)
print(not_primes)




