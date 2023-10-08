from typing import List


def hello():
    return ("Hello")


def counting_bits(n: int) -> List[int]:    
    BIT_BARRIERS = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072]
    numbers_to_bits = {}
    nearest_low_bit_barrier_index = 0
    for i in range(n+1):
        if i == 0:
            numbers_to_bits[0] = 0
            continue
        if i <= BIT_BARRIERS[nearest_low_bit_barrier_index]:
            if i & BIT_BARRIERS[nearest_low_bit_barrier_index]:
                numbers_to_bits[i] = 1
                nearest_low_bit_barrier_index += 1
            else:
                numbers_to_bits[i] = numbers_to_bits[i-BIT_BARRIERS[nearest_low_bit_barrier_index-1]] + 1

    return list(numbers_to_bits.values())

def counting_bits_simple_solution(num: int) -> List[int]:
    counter = [0]
    for i in range(1, num+1):
        counter.append(counter[i >> 1] + i % 2)
    return counter

if __name__ == "__main__":
    print(counting_bits(85723))
    print(counting_bits_simple_solution(85723))
