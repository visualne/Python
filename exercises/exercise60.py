#  N x M

#  N will be the number of rows
#  M will be the number of columns

N=7
M=21

# 0->1
# 1->3 (+2)
# 2->5 (+3)
# 3->7 (+4)
# 4->9 (+5)
# 5->11 (+6)
# 6->13 (+7)

def generate_symbols(line_num):

    symbol = '.|.'

    if line_num == 0:
        number_of_symbols = 1
    else:
        number_of_symbols = (line_num + 1) + line_num

    sample_string = ''
    for something in range(number_of_symbols):
        sample_string = sample_string + symbol

    return sample_string


#  Finding middle of doormat
if N % 2 == 0:
    middle = N / 2
else:
    middle = (N / 2) + 1

print(N)
print(middle)


for val in range(N):

    #  Generating symbols
    symbols_generated = generate_symbols(val)

    #  Checking for the middle of the mat and printing
    #  Welcome
    if val == middle - 1:
        number_of_dashes = (M - 7) / 2
        dashes = number_of_dashes * '-'
        print(dashes+'WELCOME'+dashes)

    #  Getting everything after middle of mat.
    if (val <= middle - 2):
        #  Printing vertical dashes on front and back of line.
        number_of_horizontal_dashes = (M - len(generate_symbols(val))) / 2
        horizontal_dashes = number_of_horizontal_dashes*'-'

        print(horizontal_dashes+symbols_generated+horizontal_dashes)
    else:
        pass




