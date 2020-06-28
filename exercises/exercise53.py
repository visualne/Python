# It must start with a 4,5 or 6.
# It must contain exactly 16 digits.
# It must only consist of digits (0-9).
# It may have digits in groups of 4 separated by one hyphen "-".
# It must NOT use any other separator like ' ' , '_', etc.
# It must NOT have 4 or more consecutive repeated digits.

import re

cc_inputs = [
'4123456789123456',
'5123-4567-8912-3456',
'61234-567-8912-3456',
'4123356789123456',
'5133-3367-8912-3456',
'5123 - 3567 - 8912 - 3456'
]


for cc_num in cc_inputs:
    #  Starts with a 4,5 or 6 followed by 15 digits.
    # match = r'^[4,5,6]\d{15}$|'
    match = re.match(r'^[4,5,6]\d{15}$|^[4,5,6]\d{3}\-\d{4}\-\d{4}\-\d{4}$',cc_num)

    match_repeating = re.search(r'(\d)\1{3,}|(\d)\2{1,}\-\2{1,}',cc_num)

    if match_repeating:
        print cc_num + ' is INVALID.'
        continue

    if match:
        print match.group() + ' is valid!'
    else:
        print cc_num + ' is INVALID.'


