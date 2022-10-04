def convert_roman_to_decimal(roman_number):

    decimal = 0
    anterior = ''

    for x in roman_number:
        if x == "I":
            decimal += 1
        if x == "V":
            if anterior == "I":
                decimal -= 2  
            decimal += 5
        if x == "X":
            if anterior == "I":
                decimal -= 2
            decimal += 10
        if x == "L":
            if anterior == "X":
                decimal -= 20
            decimal += 50
        if x == "C":
            if anterior == "X":
                decimal -= 20
            decimal += 100
        if x == "D":
            if anterior == "C":
                decimal -= 200
            decimal += 500
        if x == "M":
            if anterior == "C":
                decimal -= 200
            decimal += 1000

        anterior = x

    return decimal