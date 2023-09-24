toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)


print("We sell " + str(num_pizzas) + " different kinds of pizza!")

pizza_and_prices = zip(prices, toppings)
print(list(pizza_and_prices))

pizza_and_prices_sorted = sorted(zip(prices, toppings))
print(pizza_and_prices_sorted)

cheapest_pizza = pizza_and_prices_sorted[0]
print(cheapest_pizza)

priciest_pizza = pizza_and_prices_sorted[-1]
print(priciest_pizza)

pizza_and_prices_sorted.pop(-1)
print(pizza_and_prices_sorted)

toppings.append("peppers")
prices.append(2.5)
pizza_and_prices_sorted = sorted(zip(prices, toppings))
print(pizza_and_prices_sorted)

three_cheapest = pizza_and_prices_sorted[0:3]
print(three_cheapest)
