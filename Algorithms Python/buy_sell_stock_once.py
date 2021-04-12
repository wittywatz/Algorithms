def buy_and_sell_stock_once(prices):
  if(len(prices)==0):
    return None
  minimum_price = prices[0]
  max_profit = 0
  for price in prices:
    max_profit_sell_today = price - minimum_price
    # print('sell today',max_profit_sell_today)
    max_profit = max( max_profit, max_profit_sell_today)
    # print(max_profit)
    minimum_price = min( minimum_price, price)
    # print('minimum', minimum_price)
  return max_profit

print(buy_and_sell_stock_once([310,315,275,295,260,270,290,230,255,250]))