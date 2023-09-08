import math
import pandas


def currency(x):
    return f"${x:.2f}"


recipe_name = 'a+b+c'

ingredients = ['a', 'b', 'c']
units_used = ['yes', 'no', 'yes']

units_recipe = ["g", "", "ml"]
recipe_amounts_grams = [500, 0, 1200]
recipe_quantities = [500, 3, 1200]

units_store = ["g", "", "l"]
store_amounts_grams = [270, 0, 3000]
store_quantities = [270, 1, 3]

costs = [12.99, 5, 7.50]

total_cost_to_make = 0
total_cost_to_buy = 0

prices = []
costs_to_buy = []
costs_to_make = []

for item in range(len(ingredients)):

    # finds how many of the store bought item you'd need to fulfill the recipe requirements
    if units_used[item] == "yes":

        # finds out how many times the store item fits into the ingredient
        store_fits = math.ceil(float(recipe_amounts_grams[item]) / float(store_amounts_grams[item]))

        # calculates the value of each ingredient
        cost_to_make = float(costs[item]) / float(store_amounts_grams[item]) * float(recipe_amounts_grams[item])

    # if there's no units the program will pull values from the quantities lists,
    # instead of lists that measure the amounts in grams
    else:
        store_fits = math.ceil(float(recipe_quantities[item]) / float(store_quantities[item]))
        cost_to_make = float(costs[item]) / float(store_quantities[item]) * float(recipe_quantities[item])

    # finds the cost of the recipe
    cost_to_buy = store_fits * float(costs[item])

    # adds the costs of ingredients together for the total
    total_cost_to_make += cost_to_make
    total_cost_to_buy += cost_to_buy

    # adds '$' to costs after calculations are done
    price = currency(costs[item])

    # appends cost related variables to lists here, while also applying '$'s and rounding to 2 dp
    prices.append(price)
    costs_to_buy.append(currency(cost_to_buy))
    costs_to_make.append(currency(cost_to_make))

# finds the cost per serving
cost_per_serve = currency(total_cost_to_make / len(ingredients))

# adds a '$' to the total cost post calculations
total_cost_to_make = currency(total_cost_to_make)

# dictionaries of recipe, store, and costs information
recipe_dict = {

    "Ingredient:": ingredients,
    "Amount:": recipe_quantities,
    "Unit:": units_recipe
}

# dictionary for store-side variables
store_dict = {

    "Ingredient:": ingredients,
    "Amount:": store_quantities,
    "Unit:": units_store,
    "Price:": prices

}

# dictionary for money-related variables
money_dict = {

    "Ingredient:": ingredients,
    "Cost to Make:": costs_to_make,
    "Cost to buy:": costs_to_buy,

}

# turns the dictionaries into dataframes to be printed
recipe_frame = pandas.DataFrame(recipe_dict)
store_frame = pandas.DataFrame(store_dict)
costs_frame = pandas.DataFrame(money_dict)

# sets the index of the dataframes to ingredients, for easier reading
recipe_frame = recipe_frame.set_index("Ingredient:")
store_frame = store_frame.set_index("Ingredient:")
costs_frame = costs_frame.set_index("Ingredient:")

# adds
cost_per_serve = f"Cost per Serving: {cost_per_serve}\n"
total_to_make = f"Total cost to make: {total_cost_to_make}\n"
total_to_buy = f"Total cost to buy: {currency(total_cost_to_buy)}\n"

print("")
print("")

# prints the data frames as tables
print(f"|>=+--- {recipe_name} Ingredients ---+=<|")
print(recipe_frame)
print("")

print("|>=+---------- Store items ---------+=<|")
print(store_frame)
print("")

print("|>=+------------- Costs ------------+=<|")
print(costs_frame)
print("")

# prints the costs that aren't to be displayed on a per-ingredient basis
print(cost_per_serve)
print(total_to_make)
print(total_to_buy)
