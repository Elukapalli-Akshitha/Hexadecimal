def decimal_to_hexadecimal(decimal_num):
    try:
        decimal_num = int(decimal_num)
    except ValueError:
        return "Invalid input. Please enter a valid decimal number."
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    while decimal_num > 0:
        remainder = decimal_num % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        decimal_num //= 16
    return hexadecimal
decimal_number = input("Enter a decimal number: ")


print("Hexadecimal equivalent:", decimal_to_hexadecimal(decimal_number))