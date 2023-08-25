def multi_choice_checker(question, error, valid_answer):
    # Loop to keep the question going till answered properly
    while True:

        response = input(question).lower()

        for word in valid_answer:
            if response == word[:1] or response == word:
                return word

        print(error)
        print()


def units_checker(phase):
    units = ["mg", "g", "kg", "ml", "l"]
    log_units = ["mg", "ml"]

    # Loop to keep the question going till answered properly
    while True:

        if phase == "recipe":
            response = input("|>=+--- What unit is this ingredient measured in? ---+=<| \n").lower()

        else:
            response = input("|>=+--- What unit is this item measured in? ---+=<| \n").lower()

        if response == "m":

            l_or_g = multi_choice_checker("|>=+--- Did you mean ml or mg? ---+=<| \n",
                                          "|>=+--- please answer with an 'ml', or an 'mg' ---+=<| \n",
                                          log_units).lower()

            if l_or_g == "mg":
                return "mg"

            else:
                return "ml"

        else:
            for word in units:
                if response == word[:1] or response == word:
                    return word

        print("|>=+--- Please answer with one of the following: mg, g, kg, ml, or l ---+=<|")

