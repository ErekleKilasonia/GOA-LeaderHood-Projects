def backwards_prime(start, stop):
    listn = [i for i in range(start,stop+1) if primes(i) and primes(int(str(i)[::-1])) and i != int(str(i)[::-1])]
    return listn
def primes(number):
    for i in range(2,int(round(number**0.5,1))+1):
        if number % i == 0:
            return False
    return True