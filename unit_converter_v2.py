
# converts ingredient quantities to grams, for more standardized calculations
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


while True:

    unit = input("Unit = ")
    quantity = input("Quantity = ")
    converted_amount = grams_converter(quantity, unit)
    print(converted_amount, "grams")
