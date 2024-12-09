def handle_commas(x):
    no_commas = int(x.replace(",", ""))
    return no_commas


print(handle_commas("1,000,000"))
