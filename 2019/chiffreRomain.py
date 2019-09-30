
def convertEnEntier(nombre):

    result = "";
    if (nombre == 4):
        result = "IV"
    if (nombre == 3):
        result = "III"
    if (nombre == 2):
        result = "II"
    if (nombre == 1):
        result = "I"

    return result


print (convertEnEntier(1))
print (convertEnEntier(2))
print (convertEnEntier(3))

