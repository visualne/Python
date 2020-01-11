import re

# Input
# abc@example.co.uk
# abc@example.com
# abc<>@example.com
# abc@example@gmail.com
# adsfaf.....@google.com

# Output
# abc<>@example.com
# abc@example@gmail.com

# match = re.search('^[^\d][\w\-\_\+\.\,]+\@[\w\-]+\\.\w{2,3}',email)

# For simplicity, assume that a valid email address has the following rules-

    # Email should be of the form local@domain.com

    # There can only be alphanumberic characters in the local part email address.

    #  To me the above would look something like: \w+

    # The following characters are valid in the local part of the email as long as they are not the first character.
    # -, _, +, .

    # ex) ad-df_,..@google.com
    #

    #  To me the above would look something like: \-+ or \_+ or \++ \.+
    #  Could do something like this [\w+\-+\_+\++\.+]
    # Might be way to do this here: (?iLmsux)(One or more letters from the set 'i', 'L', 'm', 's', 'u', 'x'.)

    #  Email address can not start with a number.
    #  To me that sounds like: ^(?!\d).+ <--This matches any characters after the first character
    #  as long as the first character is not a digit.

    # Domain name can only contain alphanumeric characters and -. - done
    # com part can have at most one ., for e.g. co.uk or co.in is valid but as.df.gh is invalid - done

    # Very close with the below regular expression.
    # match = re.search('^[^\d\-\_\+\.\,][\w\-\_\+\.\,]+\@[\w\-]+\\.\w{2,3}$',email)


def main():
    # Incase you have to take input, please take it from file named 'input' (without quotes) [e.g. cat input]
    # Print your final output to console. Do not redirect to another file.
    # E.g. Suppose the question is to print the content of a file.
    #    Your solution should be 'os.system("cat input")'(without single quotes) instead of 'os.system("cat input > output")'. That's it!
    # Your code starts from here...

    #  Opening input file
    f = open('input','r')

    #  Reading in each line out input
    for email in f.readlines():

        #  Checking for a match
        # match = re.search(r'^(?!\d\-\_\+\.\,)[\w\-\_\+\.\,]+\@[\w\-]+\.\w{2,3}', email)

        # Learned that you can sepertate characters inside of a group.
        # example) (?\d|\-) <- This means it is not a digit or a

        # This won't work inside of a ()
        # ex) (a+|b+) it has to be this (a|b)+ <- No where in the docs that I can see explicitly states you
        # can't do this (a+|b+) how does one go about about figuring those types of things out.
        # **Correction something like the following will work (\w+$|\w+\.\w+$) Why would that work but this wouldnt
        # (\w+|\-+)**
        # I think it is because (\w+|\-+) isn't going to the end of the string unless you do this (\w+|\-+)+

        match = re.search(r'^(?!\d|\-|\_|\+|\.|\,)(\w|\-|\_|\.|\,)+\@(\w|\-)+\.(\w+$|\w+\.\w+$)',email)

        if match:
            pass
        else:
            print email


    return 0

if __name__ == '__main__':
    main()
