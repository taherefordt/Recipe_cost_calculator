def metric_converter(recipe_quantity, recipe_unit, store_unit):

    if recipe_unit == "kg" and store_unit == "g":
        converted_unit = recipe_quantity * 1000
        return converted_unit

    elif recipe_unit == "g" and store_unit == "mg":
        converted_unit = recipe_quantity * 1000
        return converted_unit

    elif recipe_unit == "mg" and store_unit == "kg":
        converted_unit = recipe_quantity * 1000000
        return converted_unit

    elif recipe_unit == "l" and store_unit == "ml":
        converted_unit = recipe_quantity * 1000
        return converted_unit

    elif recipe_unit == "mg" and store_unit == "g":
        converted_unit = recipe_quantity / 1000
        return converted_unit

    elif recipe_unit == "kg" and store_unit == "mg":
        converted_unit = recipe_quantity / 1000000
        return converted_unit

    elif recipe_unit == "g" and store_unit == "kg":
        converted_unit = recipe_quantity / 1000
        return converted_unit

    elif recipe_unit == "ml" and store_unit == "l":
        converted_unit = recipe_quantity / 1000
        return converted_unit

    else:
        converted_unit = recipe_quantity
        return converted_unit


