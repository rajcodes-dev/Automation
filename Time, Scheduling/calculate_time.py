"""calculate_time.py - Measure how long it takes to multiply 100,000 numbers."""
import time

def calculate_product():
    product = 1
    for i in range(1, 100_001):
        product = product * i
    return product

start_time = time.time()
result = calculate_product()
end_time = time.time()
print(f"It took {end_time - start_time} second to calculate.")
