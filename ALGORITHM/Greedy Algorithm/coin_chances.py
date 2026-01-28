def greedy_coin_change(amount):
    # Indian currency denominations
    coins = [ 500,  100, 50, 20, 10, 5, 2, 1]
    
    result = []

    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)

    return result


# Example
amount = 1024
coins_used = greedy_coin_change(amount)

print("Coins used:")
for c in coins_used:
    print(c)
