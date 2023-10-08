def hello():
    return ("Hello")

def reverse_bits(n: int) -> int:
    # Loop through the array for each binary place until n = 0
    return_string = '0b'
    while len(return_string) < 34:
        last_digit = n % 2
        # Add zero to last place
        if last_digit == 0:
            return_string += '0'
        # Add one to last place
        else: 
            return_string += '1'
        n = n >> 1
    return int(return_string,2)

def revers_bits_alt_solution(n: int) -> int:
    result = 0
    for _ in range(32):
        last_digit = n % 2
        if last_digit:
            result = (result << 1) + 1
        else:
            result = result << 1
        n = n >> 1
    return result

if __name__ == "__main__":
    print(reverse_bits(43261596))
    print(revers_bits_alt_solution(43261596))