def num_check(question, flint, low=None, high=None, exit_code=None):
    while True:

        # sets up error messages for floats and integers
        if flint == 'float':
            if low is not None and high is not None:
                error = "Please enter any number between {} and {} (inclusive)".format(low, high)
            elif low is not None:
                error = "Please enter any number that is more than or equal to {}".format(low)
            elif high is not None:
                error = "Please enter any number that is less than or equal to {}".format(high)
            else:
                error = "|+=- Please enter a number -=+|"

        elif flint == "int":
            if low is not None and high is not None:
                error = "Please enter an integer between {} and {} (inclusive)".format(low, high)
            elif low is not None:
                error = "Please enter an integer that is more than or equal to {}".format(low)
            elif high is not None:
                error = "Please enter an integer that is less than or equal to {}".format(high)
            else:
                error = "|+=- Please enter a whole number -=+|"

        try:

            response = input(question)

            # check to see if response is the exit code and return it
            if response == exit_code:
                return response

            # change the response into an integer or float depending on flint

            if flint == "int":
                response = int(response)

            elif flint == "float":
                response = float(response)

            # Checks response is not too low, not use of 'is not' keywords
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        # checks input is a integer
        except ValueError:
            print(error)
            continue

