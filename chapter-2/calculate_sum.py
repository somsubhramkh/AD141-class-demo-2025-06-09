#!/usr/bin/env python3

counter = 5
total = 0

while counter <= 10:
    total += counter                    # total = total + counter
    counter += 1
    if counter == 7:
        continue 
    print("Running Total =", total, "Counter =", counter)

print()
print("Final Total = ", total)