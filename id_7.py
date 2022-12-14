# https://projecteuler.net/problem=7

# This is 100% not the best solution, but I didn't want to cheat and paste someone else's code
# He copes with a specific task in adequate time, and this is the main thing to solve the problem
#   in an acceptable form, if this solution becomes unacceptable, you can always optimize


index_desired_prime_number = 10_001
# we skip the usual numbers 2, 3, 5, 7 for code simplicity
current_prime_number = 11
index_current_prime_number = 5
# if the number is a multiple of 2, 3, 5, 7 then it is not prime
# composite number can be a product of 2 prime numbers e.g. 11 * 13 = 143
dividers = [3, 5, 7, current_prime_number]


while index_current_prime_number < index_desired_prime_number:
    # step +2 to skip all multiples of 2
    current_prime_number += 2

    for i, divider in enumerate(dividers):
        if current_prime_number % divider == 0:
            break

        if i + 1 == len(dividers):
            index_current_prime_number += 1
            dividers.append(current_prime_number)

print(current_prime_number)
