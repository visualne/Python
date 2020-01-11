import re

# head
# title
# object
# -> type > application/x-flash
# -> data > your-file.swf
# -> width > 0
# -> height > 0
# param
# -> name > quality
# -> value > high

#  The next step is to print <tag only on its own line

#  Opening input file
f = open('input4','r')


def printAttributes(attributesString):
    #  Finding all the matches and printing each one of them out.
    attributes = re.findall('\w+=\"[\w\-\.\/]+\"',attributesString)
    if attributes:
        for attribute in attributes:
            #  Replacing = with >
            attribute = attribute.replace('=',' > ')
            #  Replacing " with nothing
            attribute = attribute.replace('\"','')

            #  Printing final string in this format
            #  attribute > some_value
            print ' -> ' + attribute

#  Reading each line of input in the input file
for val in f.readlines():

    #  Regular expressions created to pull classify each type of line
    # ex) openingTag = <html>
    # ex) noClosingTagOnLine = <object whatever
    # ex) attributeOnly =   data = "whatever"
    # ex) attributesOnlyAndClosingTag = <param name="whatever value="as"/>
    openingTag = re.match(r'<(\w+)>',val)
    noClosingTagOnLine = re.match(r'<([A-Za-z]+) ([\w\=\"\/\-]+)',val)
    attributeOnly = re.match(r'\s\s\w.*?\n',val)
    attributesOnlyAndClosingTag = re.match(r'\s\s<([A-Za-z]+)\s([\w\=\"\/\-\s]+>)',
                                          val)

    #  If statements to pull out the needed values from the line
    if openingTag:
        print openingTag.group(1)
    elif noClosingTagOnLine:
        print noClosingTagOnLine.group(1)
        # [attribute1 = "1", attribute2 = "2"]
        printAttributes(noClosingTagOnLine.group(2))
    elif attributeOnly:
        # [attribute1 = "1", attribute2 = "2"]
        printAttributes(attributeOnly.group())
    elif attributesOnlyAndClosingTag:
        #  If string was <param attribute1=a attribute1=b/>
        #  attributesOnlyAndClosingTag.group(1) will print
        print attributesOnlyAndClosingTag.group(1)
        # [attribute1 = "1", attribute2 = "2"]
        printAttributes(attributesOnlyAndClosingTag.group(2))
    else:
        pass


