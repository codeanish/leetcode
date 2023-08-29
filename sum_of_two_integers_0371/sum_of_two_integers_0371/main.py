from operator import*

# In python you can use the add operator in your code. This just computes a + b, 
# but the addition is in a python library rather than my code. Doesn't seem like what the solution is looking for.
def get_sum_not_in_the_spirit(a: int, b: int) -> int:
    return add(a,b)

def get_sum(a: int, b: int) -> int:
    if a == 0:
        return b
    if b == 0:
        return a
    
    mask = 0xffffffff
    while(b & mask != 0):
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    return a & mask if b > mask else a

if __name__ == "__main__":
    print(get_sum(2,3))