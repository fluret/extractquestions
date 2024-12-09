def normalize_name(text):
    new_string = text.strip("0123456789 ").lower().replace(" ", "_")
    output = ""
    if new_string.isidentifier():
        print(new_string, "is a valid identifier")
        for i in new_string:
            if i not in "!@#$%^&*()+=-[]{}\/|?.<>,`~":
                output += i
    else:
        print(new_string, "is NOT a valid identifier")
    return print(output)


normalize_name("one+one")
normalize_name(" Dani Bojado ")
