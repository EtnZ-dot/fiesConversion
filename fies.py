# EtnZ

def celsius_to_fies(num_input):
    num = round((8.1075 + num_input) / 54.05, 2)
    return num


def fies_to_celsius(num_input):
    num = round(54.05 * num_input - 8.1057, 2)
    return num
