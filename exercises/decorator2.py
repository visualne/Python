import re

# phone = ['07895462130','919875641230','9195969878','+919275123230']

def wrapper(f):
    def fun(l):
        for index in range(len(l)):
            #  Check to see if number starts with 91
            nine_one_match_ten_digits = re.match(r'^(91)(\d{5})(\d{5})',\
                                                 l[index])
            plus_nine_one_match_ten_digits = re.match(r'^(\+91)(\d{5})(\d{5})',\
                                                      l[index])
            zero_match_ten_digits = re.match(r'^(0)(\d{5})(\d{5})',l[index])
            non_prefix_ten_digits = re.match(r'(\d{5})(\d{5})',l[index])

            if nine_one_match_ten_digits:
                # printing good string
                l[index] = '+' + nine_one_match_ten_digits.group(1) + ' ' + \
                    nine_one_match_ten_digits.group(2) + ' ' + \
                        nine_one_match_ten_digits.group(3)
            elif plus_nine_one_match_ten_digits:
                l[index] = plus_nine_one_match_ten_digits.group(1) + ' ' + \
                      plus_nine_one_match_ten_digits.group(2) + ' ' + \
                      plus_nine_one_match_ten_digits.group(3)
            elif zero_match_ten_digits:
                l[index] = '+91' + ' ' + \
                      zero_match_ten_digits.group(2) + ' ' + \
                      zero_match_ten_digits.group(3)
            elif non_prefix_ten_digits:
                l[index] = '+91' + ' ' + \
                        non_prefix_ten_digits.group(1) + ' ' + \
                      non_prefix_ten_digits.group(2)
            else:
                pass

        #  Calling original function with the new sorted list
        return f(l)
    #  Returning decorated function that will clean the values in the list.
    return fun


@wrapper
def sort_phone(l):
    print '\n'.join(sorted(l))

if __name__ == '__main__':
    # l = [raw_input() for _ in range(int(input()))]
    l = ['07895462130', '919875641230', '9195969878', '+919275123230']
    sort_phone(l)