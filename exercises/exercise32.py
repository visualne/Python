import re

phone = ['07895462130','919875641230','9195969878','+919875641230']
print phone

for num in phone:
    #  Check to see if number starts with 91
    nine_one_match_ten_digits = re.match(r'^(91)(\d{10})',num)
    plus_nine_one_match_ten_digits = re.match(r'^(\+91)\d{5}\d{5}',num)
    zero_match_ten_digits = re.match(r'^(0)(\d{10})',num)
    non_prefix_ten_digits = re.match(r'\d{10}',num)

    if nine_one_match_ten_digits:
        # print nine_one_match_ten_digits.group()

        # printing good string
        print '+' + nine_one_match_ten_digits.group(1) + ' ' + \
            nine_one_match_ten_digits.group(2)

    elif non_prefix_ten_digits:
        print non_prefix_ten_digits.group()
    elif plus_nine_one_match_ten_digits:
        print plus_nine_one_match_ten_digits.group()
    else:
        print zero_match_ten_digits.group()




