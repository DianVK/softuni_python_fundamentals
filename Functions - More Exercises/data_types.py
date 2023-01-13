def check_data_type(inp_type, el):
    result = ""
    if inp_type == "int":
        result = f"{int(el) * 2:.0f}"
    elif inp_type == "real":
        result = f"{float(el) * 1.5:.2f}"
    elif inp_type == "string":
        result = "$" + el + "$"
    return result


data_type = input()
element = input()
print(check_data_type(data_type, element))
