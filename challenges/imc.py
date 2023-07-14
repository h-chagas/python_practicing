first_name = "Hugo"
surname = "Cidral das Chagas"
pronoum = "his"
height = 1.68
weight = 90

imc_result = weight / (height * height)

def imc_range(imc):
    if imc < 18.5:
        return "underweight"
    elif imc >= 18.5 and imc < 25.0:
        return "healthy weight"
    elif imc >= 25.0 and imc < 30.0:
        return "overweight"
    else:
        return "obesity" 

imc_definition = imc_range(imc_result)

print("%s's IMC is %d, which means %s is in the %s range."%(first_name, imc_result, pronoum, imc_definition))


## f-strings formatting
sentence1 = f"{first_name} {surname} is {height} height and is {weight} kg., {pronoum} IMC is {imc_result:.2f} which is in the {imc_definition} range"
print("F-STRING ---->", sentence1)


# format function
sentence2 = "{} {} is {} height and is {} kg., {} IMC is {:.2f} which is the {} range.".format(first_name, surname, height, weight, pronoum, imc_result, imc_definition)
print("FORMAT FUNCTION ---->", sentence2)


# format function by index
sentence3 = "{1} {0} is {2} height and is {3} kg., {4} IMC is {5:.2f} which is the {6} range.".format(first_name, surname, height, weight, pronoum, imc_result, imc_definition)
print("FORMAT FUNCTION BY INDEX ---->", sentence3)

# named parameter
sentence4 = "{name} {last_name} is {info1} height and is {info2} kg., {info3} IMC is {info4:.2f} which is the {info5} range.".format(
    name=first_name, 
    last_name=surname, 
    info1=height, 
    info2=weight, 
    info3=pronoum, 
    info4=imc_result, 
    info5=imc_definition
    )
print("FORMAT FUNCTION WITH NAMED PARAMETER ---->", sentence4)