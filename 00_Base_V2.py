import pandas
import math


# grams_converter converts any unit to grams, this allows for a more standard calculation process
def grams_converter(ingredient_quantity, ingredient_unit):

    # dictionary of units and their size relative to grams, these are used for the conversion
    # this works on the assumption that: 1ml = 1g
    conversion_factors = {
        "mg": 0.001,
        "g": 1,
        "kg": 1000,
        "ml": 1,
        "l": 1000
    }

    # finds the weight of the ingredient (in grams) from multiplying it by the factor above
    weight_grams = float(conversion_factors[ingredient_unit]) * float(ingredient_quantity)

    # returns the converted quantity
    return weight_grams


# num_check allows the user to input a float or int, and returns it.
# if the response is neither it sends an error and tries again
def num_check(question, flint, low=None, exit_code=None):
    while True:

        # if the number doesn't need a low, a different error is generated compared to when there is one
        if low is not None:
            error = f"|>=+--- Please enter a number that is more than or equal to {low} ---+=<|"

        else:
            error = "|>=+--- Please enter a number ---+=<|"

        # continues to attempt code below until a valid answer is given
        try:
            response = input(question)

            # check to see if response is the exit code and return it
            if response == exit_code:
                return response

            # change the response into an integer or float depending on flint
            if flint == "int":
                response_conv = int(response)

            else:
                response_conv = float(response)

            # Checks response is not too low, not use of 'is not' keywords
            if low is not None and response_conv < low:
                print(error)
                continue

            return response

        # checks input is a number, if not sends an error
        except ValueError:
            print(error)

            continue


# a pre typed set of instructions that is called upon later.
def instructions():
    print('''\n
|>=+------------- instructions --------------=+<|
y

''')


# returns anything the user responds with so long as it's not blank
def not_blank(question):
    # loop to repeat until a valid answer is received
    while True:

        response = input(question)

        # if the response is blank, print an error
        if response == "":
            print("|>=+--- Your response to this cannot be blank ---+=<|")

        # if the response is not blank return response
        else:
            return response


# this function is able to ask a question to the user
# if the answer they respond with is valid for the question the program returns it
def multi_choice_checker(question, valid_answer, error):
    # Loop to keep the question going till answered properly
    while True:

        response = input(question).lower()

        # checks if the user response is one of the valid answers
        for word in valid_answer:

            # if the response shares the same first letter or is the same word, the program returns the answer
            if response == word[:1] or response == word:
                return word

        print(error)


# this function checks what unit a specific ingredient is measured in
def units_checker(phase, ingredient):
    # list of valid units
    unit_list = ["mg", "g", "kg", "ml", "l"]

    # log = L or G = Liquid Or Solid
    log_units = ["mg", "ml"]

    # Loop to keep the question going till answered properly

    while True:

        if phase == "recipe":

            response = multi_choice_checker(f"|>=+--- What unit is {ingredient} measured in? ---+=<| ", unit_list,
                                            "|>=+--- please answer with any of the following: ml, l, mg, g, kg ---+=<|"
                                            ).lower()

        else:
            response = multi_choice_checker(f"|>=+--- What unit is '{ingredient}' measured in? ---+=<| ", unit_list,
                                            "|>=+--- please answer with any of the following: ml, l, mg, g, kg ---+=<|"
                                            ).lower()

        if response == "m":

            l_or_g = multi_choice_checker("|>=+--- Did you mean ml or mg? ---+=<| ", log_units,
                                          "|>=+--- please answer with any of the following: ml, l, mg, g, kg ---+=<|"
                                          ).lower()

            if l_or_g == "mg":
                return "mg"

            else:
                return "ml"

        elif response in unit_list:

            for word in unit_list:
                if response == word[:1] or response == word:
                    return word

        else:
            print("|>=+--- please answer with any of the following: ml, l, mg, g, kg ---+=<|")


# converts floats to numbers rounded to 2 dp
def currency(x):
    return f"${x:.2f}"


# lists for valid answers
units = ["mg", "g", "kg", "ml", "l"]
yes_no = ["yes", "no"]

# these lists are used to differentiate between solids and liquids
solid = ['mg', 'g', 'kg']
liquid = ['ml', 'l']

# lists for ingredient variables
ingredients = []
units_used = []
recipe_quantities = []
recipe_amounts_grams = []
units_recipe = []

# lists for store-side variables
store_quantities = []
store_amounts_grams = []
units_store = []
costs = []
prices = []

# lists for recipe costs
units_or_not = []
costs_to_buy = []
costs_to_make = []

total_cost_to_make = 0
total_cost_to_buy = 0


print("/>=+-----------------------------------------------+=<\\")
print("|>=+--- Welcome, to the Recipe Cost Calculator! ---+=<|")
print("\\>=+-----------------------------------------------+=</")
print("")

# asks the user if they want to see instructions on how to use the program
show_instructions = multi_choice_checker("|>=+---- Would you like to look at the instructions? ----+=<| ",
                                         yes_no, "|>=+--- Please answer with a yes or no ---+=<|")
# prints the instructions if yes
if show_instructions == "yes":
    instructions()

# gets the name of the recipe from the user
recipe_name = not_blank("|>=+--- What is the name of your dish? ---+=<| ")

print("")

# 'servings' is used to find the cost per serving of the final dish
servings = num_check("|>=+--- How many does this recipe serve? ---+=<| ", "float", 1, None)

# this loop of code finds the
# - name of ingredient
# - unit of ingredient (and whether they're used)
# - quantity of ingredient (in units or as a count)

while True:

    print("")
    print("")

    # if the user hasn't named any ingredients, exit code is None
    if not ingredients:
        ingredients_question = "|>=+--- Ingredient Name: ---+=<| "
        exit_code_recipe = None

    else:
        ingredients_question = "|>=+--- Ingredient Name (type 'xxx' start entering in-store information): ---+=<| "
        exit_code_recipe = "xxx"

    # Asks the user for an ingredient and adds it to a list
    recipe_ingredient = not_blank(ingredients_question)

    # if the ingredient name is equal to the exit code, starts the store phase
    if recipe_ingredient == exit_code_recipe:
        break

    print("")

    # asks if the ingredient is measured in units
    units_usage = multi_choice_checker("|>=+--- Is this ingredient measured in units? ---+=<| ",
                                       yes_no, "|>=+--- Please answer with a yes or no ---+=<| ")

    print("")

    # if the ingredient is measured in units:
    if units_usage == "yes":
        # finds the unit that the recipe measures ingredients in
        recipe_unit = units_checker("recipe", recipe_ingredient)
        print("")

        # finds the amount of ingredient needed in said unit
        recipe_amount = num_check(f"|>=+--- Ingredient Amount ({recipe_unit}): ---+=<| ", "float",
                                  1, None)

    # if units aren't used for the ingredient
    else:
        # then recipe unit is "<blank>" to allow for use of indexes
        recipe_unit = ""

        # finds the amount of ingredient needed in said unit
        recipe_amount = num_check(f"|>=+--- Number of {recipe_ingredient}s: ---+=<| ", "float",
                                  1, None)

    # if units are used for an ingredient, converts the quantity to grams
    if units_usage == "yes":
        # finds the recipe quantity in grams for calculations later
        recipe_amount_grams = grams_converter(recipe_amount, recipe_unit)

    else:
        recipe_amount_grams = ""
        pass

    # appends above info to their individual lists, includes:
    # - ingredient name
    # - ingredient unit
    # - ingredient amount (in said unit)
    # - ingredient amount (in grams)
    # - whether units are used or not

    ingredients.append(recipe_ingredient)
    units_recipe.append(recipe_unit)
    recipe_quantities.append(recipe_amount)
    recipe_amounts_grams.append(recipe_amount_grams)
    units_used.append(units_usage)


# loops the next questions the same number of times as there are ingredients
for item in range(len(ingredients)):

    print("")

    # finds the cost of each ingredient
    price = num_check(f"|>=+--- Cost of {ingredients[item]}: ---+=<| $", "float", 0, None)

    # stops name 'store_unit' from being undefined
    store_unit = ""

    if units_used[item] == "yes":

        # invalid units makes sure that the loop runs until a valid answer is given
        invalid_units = "yes"

        # loop to keep next chunk going until a valid unit is given
        while invalid_units == "yes":

            # gets the recipe unit for the nth ingredient
            recipe_unit = units_recipe[item]

            # get the store-side unit from the user
            store_unit = units_checker("store", ingredients[item])

            # if the recipe has a solid ingredient, and its liquid in store or vice-versa creates an error

            # checks if the nth unit in the recipe list is solid or liquid
            if recipe_unit in solid:

                # if the recipe unit is solid, and the store unit is liquid, raises an error
                if store_unit in liquid:
                    print("|>=+--- This item must be solid (mg, g, or kg) ---+=<|")
                    # keeping invalid_units as "yes" keeps the loop going
                    invalid_units = "yes"

                # if both are solid the program continues
                else:
                    invalid_units = "no"

            # if the unit is not in solid it can only be in liquid
            else:

                # if the units contradict again, the program
                if store_unit in solid:
                    print("|>=+--- This item must be liquid (ml, or l) ---+=<|")
                    invalid_units = "yes"

                else:
                    invalid_units = "no"
    else:
        pass

    # finds the quantity of the item in store
    store_amount = num_check("|>=+--- Store-bought Amount: ---+=<| ", "float", 0, None)

    # if units are used for this ingredient
    if units_used[item] == "yes":
        # finds store quantity in grams for calculations
        store_amount_grams = grams_converter(store_amount, store_unit)
        store_amounts_grams.append(store_amount_grams)

    else:
        # making 'store_amount_grams' = "<blank>" here
        # this allows me to use indexes with ingredients that do and don't have units
        store_amount_grams = ""
        store_amounts_grams.append(store_amount_grams)
        pass

    # appends the store values to lists
    costs.append(float(price))
    store_quantities.append(store_amount)
    units_store.append(store_unit)


# this loop of code figures out how much each recipe item costs, as well as most other things cost related
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
cost_per_serve = f"Cost per Serving: {cost_per_serve}"
total_to_make = f"Total cost to make: {total_cost_to_make}"
total_to_buy = f"Total cost to buy: {currency(total_cost_to_buy)}"

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


# turns the dataframes into strings so that they can be written to a file
recipe_txt = pandas.DataFrame.to_string(recipe_frame)
store_txt = pandas.DataFrame.to_string(store_frame)

# assigns the dataframes + addons to lists for an easier time writing to file
to_write_1 = [recipe_name, f"|>=+--- {recipe_name} Ingredients ---+=<|", recipe_txt]
to_write_2 = ["|>=+------- Store items -------+=<|", store_txt]
to_write_3 = [cost_per_serve, total_to_make, total_to_buy]

# opens a file by the name of the recipe
file_name = f"{recipe_name}.txt"
text_file = open(file_name, "w+")

# adds the variables dictated above to the text file for all 3 dataframes
for item in to_write_1:
    text_file.write(str(item))
    text_file.write("\n\n")
for item in to_write_2:
    text_file.write(str(item))
    text_file.write("\n\n")

for item in to_write_3:
    text_file.write(str(item))
    text_file.write("")

# closes the text file
text_file.close()
