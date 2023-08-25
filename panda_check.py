import pandas

all_names = ["a", "b"]
all_costs = [4, 5]
all_surcharge = [1, 2]

# dictionary
my_dict = {
    "Name": all_names,
    "Costs": all_costs,
    "Surcharge": all_surcharge
}

my_frame = pandas.DataFrame(my_dict)

print(my_frame)
