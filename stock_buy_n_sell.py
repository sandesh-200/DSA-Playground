def max_profit_one_transaction(prices):
    if not prices or len(prices)<2:
        return 0
    
    min_price = prices[0]
    max_profit = 0

    for p in prices[1:]:
        if p<min_price:
            min_price = p
        
        else:
            profit = p-min_price
            if profit > max_profit:
                max_profit = profit

    return max_profit,f"Buy for {min_price} and sell for {max_profit+min_price}"

print(max_profit_one_transaction([7]))