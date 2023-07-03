first_name = "Hugo"
surname = "Cidral das Chagas"
pronoum = "he"
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
