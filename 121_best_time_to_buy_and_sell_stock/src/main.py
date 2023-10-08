from typing import List


def max_profit(prices: List[int]) -> int:
    profit = 0
    for day, price in enumerate(prices):
        buy_price = price
        for sell_price in prices[day + 1:]:
            profit = max(profit, sell_price - buy_price)
    return profit


def max_profit_optimised(prices: List[int]) -> int:
    profit = 0
    buy_price = prices[0]
    for sell_price in prices[1:]:
        if sell_price > buy_price:
            profit = max(profit, sell_price - buy_price)
        else:
            buy_price = sell_price
    return profit

if __name__ == "__main__":

    print(max_profit([7,1,5,3,6,4]))
    print(max_profit([3,11,1,10,5,2,5]))

    print(max_profit_optimised([7,1,5,3,6,4]))
    print(max_profit_optimised([3,11,1,10,5,2,5]))