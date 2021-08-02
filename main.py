from collatz_calculator import collatz

input = 100

result = input

while result != 1:
    result = collatz.next_collatz(result)
    print(result)