from multi_choice_check import multi_choice_checker


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


