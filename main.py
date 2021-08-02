from collatz_calculator import collatz

results = []


inputs = range(10000)

for input in inputs:
    result = input

    while result != 1:
        result = collatz.next_collatz(result)

        if result not in results:
            results.append(result)
        else:
            print("Already calculated")
            break;

        print(result)

print("Done!")