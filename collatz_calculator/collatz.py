def even_collatz(number):
    return number / 2

def odd_collatz(number):
    return (3 * number) + 1

def next_collatz(number):
    if (number % 2) == 0:
        return even_collatz(number)
    else: 
        return odd_collatz(number)