def hamming_weight_crude_method(n: int) -> int:
    binary_string = bin(n)

    hamming_weight = 0
    for character in binary_string:
        if character == '1':
            hamming_weight += 1
    return hamming_weight


def hamming_weight_bitwise_method(n: int) -> int:
    # Do this for 32 bit integer
    hamming_weight = 0
    while n > 0:
        # Taking the modulus 2 of n will give 0 or 1 if it's odd or even
        # hamming_weight += n % 2
        
        # Can also use the bitwise AND operator & with 1 to check if last bit is = 1
        hamming_weight += n & 1
        # Shift the bits one to the right 1 0 0 1 becomes 0 1 0 0
        n = n >> 1
    return hamming_weight

def hamming_weight_bitwise_optimised(n: int) -> int:
    hamming_weight = 0
    while n:
        n = n & (n-1)
        hamming_weight += 1
    return hamming_weight

import collections
import random
def hamming_weight_counter(n: int) -> int:
    
    counter = collections.Counter(bin(n)[2:])
    return counter.get("1", 0)

# def cache_weights(max_int: int):
#     for i in range(max_int):
#         hamming_weights[i+1] = hamming_weight_bitwise_optimised(i+1)

# hamming_weights = {}

# def hamming_weight_cached(n: int) -> int:
#     return hamming_weights[n]

if __name__ == "__main__":
    import time
    test_iterations = 1000000
    
    test_values = []
    for _ in range(test_iterations):
        test_values.append(random.randint(1,0x7FFFFFFF))

    start = time.perf_counter()
    for i in test_values:
        hamming_weight_crude_method(i)
    end = time.perf_counter()
    print(f"Completed hamming_weight_crude_method(rand) {test_iterations} in {end-start:0.4f} seconds")

    start = time.perf_counter()
    for i in test_values:
        hamming_weight_bitwise_method(i)
    end = time.perf_counter()
    print(f"Completed hamming_weight_bitwise_method(rand) {test_iterations} in {end-start:0.4f} seconds")
    
    # start = time.perf_counter()
    
    # cache_weights(0xFFFFFF)
    # end = time.perf_counter()
    # print(f"Done caching weights in {end-start:0.4f} seconds")

    

    start = time.perf_counter()
    for i in test_values:
        hamming_weight_bitwise_optimised(i)
    end = time.perf_counter()
    print(f"Completed hamming_weight_bitwise_optimised(rand) {test_iterations} in {end-start:0.4f} seconds")

    # import os, psutil
    # process = psutil.Process()
    # print(process.memory_info())

    # start = time.perf_counter()
    # for i in test_values:
    #     hamming_weights[i]
    #     # hamming_weight_bitwise_optimised(random.randint(0,0x7FFFFFFF))
    # end = time.perf_counter()
    # print(f"Completed hamming_weights cached(rand) {test_iterations} in {end-start:0.4f} seconds")

    # start = time.perf_counter()
    # for i in range(test_iterations):
    #     hamming_weight_counter(1000000000)
    # end = time.perf_counter()
    # print(f"Completed hamming_weight_counter(1000000000) {test_iterations} in {end-start:0.4f} seconds")