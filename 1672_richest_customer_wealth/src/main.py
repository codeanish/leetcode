from typing import List


def hello():
    return ("Hello")


def maximum_wealth(accounts: List[List[int]]) -> int:
    max_wealth = 0
    for customer in accounts:
        customer_wealth = 0
        for balance in customer:
            customer_wealth += balance
        if customer_wealth > max_wealth:
            max_wealth = customer_wealth
    return max_wealth

if __name__ == "__main__":
    print(maximum_wealth([[1,5],[7,3],[3,5]]))