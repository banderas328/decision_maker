number_of_values = int(input("enter number of values:"))
i = 0
values = []
parameters_final = []

while i < number_of_values :
    value_name = input("enter value name:")
    values.append(value_name)
    parameter = input("input parameter:")
    parameter_weight = input("enter parameter weight")
    parameter_cost = input("enter parameter cost")
    anouther_one_parameter = input("anouther one parameter ? y/n")
    parameter = str(parameter)
    parameters = {'name': parameter, 'weight': parameter_weight, "i": i , "parameter_cost" : parameter_cost}
    parameters_final.append(parameters)
    while anouther_one_parameter.lower() == "y":
        parameter = input("input parameter:")
        parameter_weight = input("enter parameter weight")
        parameter_cost = input("enter parameter cost")
        parameter = str(parameter)
        parameters = {'name': parameter, 'weight' :parameter_weight , "i" : i , "parameter_cost" : parameter_cost}
        parameters_final.append(parameters)
        anouther_one_parameter = input("anouther one parameter ? y/n")
    i += 1

i = 0

result = []

for parameter in parameters_final:
    name = parameter.get("name")
    weight = parameter.get("weight")
    parameter_cost = parameter.get("parameter_cost")
    i = parameter.get("i")
    print(weight)
    print(parameter_cost)
    print(parameter)
    total_weight = float(weight)*float(parameter_cost)
    result_value = {"i": i, "total_weight" : total_weight}
    result.append(result_value)


output = {}

for value in result:
    # print(value.get("i"))
    # print()
    i = value.get("i")
    parameter_total_weight  = value.get("total_weight")
    print(parameter_total_weight)
    if i in output:
        weight_old = output[i]
    else :
        weight_old = 0
    print(weight_old)
    weight_sum = weight_old + parameter_total_weight
    print(weight_sum)
    dict = {i: weight_sum}



    output.update(dict)

print(output)








