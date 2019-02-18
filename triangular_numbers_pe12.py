# helper function
def primes(n):
    for i in range(2,int(n/2)):
        if n % i == 0:
            return False
    return True
    
# another helper function
def genprimes(target):
    primes_list = []
    num = 2
    while len(primes_list) <= target:
        if primes(num):
            primes_list.append(num)
        num += 1
    return primes_list

# First, we need to completely factor the number into its prime numbers
def complete_prime_factorization(n):
    list_of_factors = []
    i = 2
    while n > 1:
        while n % i == 0:
            list_of_factors.append(i)
            n /= i
        i += 1
    return list_of_factors
    
# Tau function returns the total number of factors (not just primes)
def tau(n):
    list_of_factors = complete_prime_factorization(n)
    factors = {factor for factor in list_of_factors}
    counts = [list_of_factors.count(factor) for factor in factors]
    num_factors = 1
    for count in counts:
        num_factors *= (count + 1)
    return num_factors

# To generate the list of primes, we call the sieve function
def find_min_num_with_n_factors(n, n_primes = 15):
    tau_exponents = complete_prime_factorization(n)
    tau_exponents = [exponent - 1 for exponent in tau_exponents]
    tau_exponents = sorted(tau_exponents, reverse = True)
    primes_list = genprimes(n_primes)
    base_n_exp = list(zip(tau_exponents, primes_list))
    num = 1
    for pair in base_n_exp:
        num *= (pair[1]**pair[0])
    return num
    
def check_if_triangular(n):    
    total = 0
    for i in range(1,n):
        total += i
        if total == n:
            return True
        if total > n:
            return False

def find_initial_triangular_num(num_factors): #needs to take an argument here
    total = 0
    i = 1
    while total < find_min_num_with_n_factors(num_factors) : #put a more modular solution here
        total += i
        i += 1
    return total, i    

def find_minimum_triangular_number_w_n_factors(n):
    tri_num, incrementer = find_initial_triangular_num(n)
    while tau(tri_num) != n:
        tri_num += incrementer
        incrementer += 1
    return tri_num  