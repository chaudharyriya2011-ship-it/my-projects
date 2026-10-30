number = int(input("Enter a decimal number: "))

binary_result = ""

while number > 0:
    remainder = number % 2
    binary_result = str(remainder) + binary_result
    number = number // 2

print( binary_result)