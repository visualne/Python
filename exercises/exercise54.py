def add_spaces_remove_zeros(value,len_of_binary_value):

    #  Removing zero from front of string
    if value.startswith('0'):
        value = value[1:]

    #  Checking to see if the length of the value
    #  sent in is >= len_of_binary_value If it is
    #  once space will be added to the front of the string
    if len(value) >= len_of_binary_value:
        value = ' ' + value

    #  Returning value
    return value


len_of_binary_value = len(bin(17)[2:])


number_of_spaces = '%'+str(len_of_binary_value+1)+'s'

#  For loop to convert the decimal number associated with val.
for val in range(1,17+1):

    decimal_value = str(val)
    octal_value = str(oct(val))
    hex_value = str(hex(val).upper()[2:])
    bin_value = str(bin(val)[2:])

    decimal = add_spaces_remove_zeros(decimal_value,len_of_binary_value)
    num_spaces_one_less = '%'+str(len_of_binary_value)+'s'
    decimal = num_spaces_one_less % decimal

    octal = add_spaces_remove_zeros(octal_value, len_of_binary_value)
    octal = number_of_spaces % octal

    hexadecimal = add_spaces_remove_zeros(hex_value, len_of_binary_value)
    hexadecimal = number_of_spaces % hexadecimal

    binary = add_spaces_remove_zeros(bin_value, len_of_binary_value)
    binary = number_of_spaces % binary


    # if len(decimal) or len(octal) or
    # print(decimal + octal + hexadecimal)
    print(decimal + octal + hexadecimal + binary)