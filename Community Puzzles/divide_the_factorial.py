###################################
#                                 #
#   CodinGame Community Puzzles   #
#      Divide the Factorial       #
#                                 #
###################################


a, b = [int(i) for i in input().split()]

def erathosphenes(upper_limit):
    primes_to_limit = []
    is_a_prime = [True] * (upper_limit + 1)
    is_a_prime[0] = False
    is_a_prime[1] = False
    counter = 2
    while counter <= upper_limit:
        inner_counter = 2        
        while inner_counter * counter <= upper_limit:
            is_a_prime[inner_counter * counter] = False
            inner_counter += 1
        if counter >= upper_limit:
            break
        counter += 1
        while is_a_prime[counter] == False:
            if counter == upper_limit:
                break
            else:
                counter += 1
    for j in range(1, upper_limit + 1):
        if is_a_prime[j] == True:
            primes_to_limit.append(j)
    return primes_to_limit

def trial_division(number_to_crunch):
    if number_to_crunch < 2:
        return []
    prime_factors = []
    for counter in erathosphenes(int(number_to_crunch**0.5)):
        if counter ** 2 > number_to_crunch: 
            break
        while number_to_crunch % counter == 0:
            prime_factors.append(counter)
            number_to_crunch //= counter
    if number_to_crunch > 1:
        prime_factors.append(number_to_crunch)
    return prime_factors

coprimes = trial_division(a)
set_of_values = []

for k in range(len(coprimes)):
    power_over_9000 = 1
    while coprimes[k] ** power_over_9000 < b:
        power_over_9000 += 1
    if power_over_9000 == 1:
        b_factorial = 1     
        counter = b
        while counter > 0:
            b_factorial *= counter
            counter -= 1
        if b_factorial % coprimes[k] == 0:
            divisors = 1
        else:
            divisors = 0
    else:
        divisors = 0
        divisible = b
        while divisible > 0:
            divisible //= coprimes[k]
            divisors += divisible
    set_of_values.append(divisors)
    
multipliers_set = []
coprimes_shrunk = []
set_of_values_shrunk = []
multiplier = 1
test_value = coprimes[0]
for i in range(1, len(coprimes)):
    if coprimes[i] == test_value:
        multiplier += 1
    else:
        coprimes_shrunk.append(test_value)
        test_value = coprimes[i]
        multipliers_set.append(multiplier)
        multiplier = 1
        set_of_values_shrunk.append(set_of_values[i-1])
multipliers_set.append(multiplier)
coprimes_shrunk.append(coprimes[-1])
set_of_values_shrunk.append(set_of_values[-1])

divisors = set_of_values_shrunk[0] // multipliers_set[0]
for i in range(len(coprimes_shrunk)):
    test_value = set_of_values_shrunk[i] // multipliers_set[i]
    if divisors > test_value:
        divisors = test_value

print(divisors)  