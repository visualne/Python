#  N x M

#  N will be the number of rows
#  M will be the number of columns

N=7
M=21

def generate_symbols(line_num):

    if line_num == 0:
        number_of_symbols = 1
    else:
        number_of_symbols = line_num + 2

    sample_string = ''
    for something in range(number_of_symbols):
        sample_string = sample_string + symbol

    return sample_string

symbol = '.|.'

for val in range(N):

    #  Generating symbols
    symbols_generated = generate_symbols(val)

    #  Printing vertical dashes on front and back of line.
    number_of_horizontal_dashes = (M - len(generate_symbols(val))) / 2
    horizontal_dashes = number_of_horizontal_dashes*'-'

    print(horizontal_dashes+symbols_generated+horizontal_dashes)