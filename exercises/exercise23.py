# a = [9,5,1,2,6]



#  Inner for loop 0 - 4 Initial List = [9,5,1,2,6]
#  First pass: 9,5 (indexes 0 and 1) are compared. 9 will switch with 5
#  Second pass: 9,1 (indexes (1 and 2) are compared, 9 will switch with 1
#  Third pass: 9,2 (indexes 2 and 3)are compared, 9 will switch with 2
#  Fourth pass: 9,6 (indexes 3 and 4) are compared, 9 will switch with 6

#  Inner for loop 0 - 3 Initial List = [5,1,2,6,9]
#  First pass: 5,1 (indexes 0 and 1) are compared. 5 will switch with 1
#  Second pass: 5,2 (indexes 1 and 2) are compared. 2 will switch with 5
#  Third pass: 5,6 (indexes 2 and 3) are compared. no switch\

#  Find the second to lowest grade in the class
#  Sorted List = [['gerry', 10], ['larry', 50], ['rita', 80], ['joe', 90]]
#  Need a little code to determine starting position. Because
#  you are assuming that the second position in the array is the lowest.
#  ex)
#  arr = [1,4,5,6,9,10]
#
#
#
#  Dealing with these cases: arr = [1,1,4,5,6,9,10]
#
#  The below for loop find the first position of the second to lowest
#  score.
#  ex) arr = [1,1,4,5,6,9,10]

#  List of person and grade
# studentAndGrade = [['gerry',10],['larry',50],['joe',90],['rita',80],\
#                    ['claude',50]]

# studentAndGrade = [['Rachel',-50],['Mawer',-50],['Sheen',-50],\
#                    ['Shaheen',51]]

def printListOfNames(secondToLowestScoreList):
    #  Printing the names of the students that have the second lowest grade
    for student in secondToLowestScoreList:
        print student[0]


studentAndGrade = [['Test1',52],['Test2',53],['Test3',53]]


#  The below bubble sort sorts all the students from lowest to highest.
for i in range(len(studentAndGrade)-1,-1,-1):
    #  For loop to compare two values and moves one if necessary.
    for j in range(0,i):
        #  Comparing two values in the list. If the lower positioned (a[j])
        #  element is greater then a[j+1] move it to a[j+1]
        if studentAndGrade[j][1] > studentAndGrade[j+1][1]:
            temp = studentAndGrade[j]
            studentAndGrade[j] = studentAndGrade[j+1]
            studentAndGrade[j+1] = temp

#  This for loop finds the index of the second to lowest score.
#  Can't figure out a way to get around this. This deals with cases
#  like the following: In
#  [['whatever',74],['asasdaf',74],['asasdaf',79],['asasdaf',80]]
lowestScore = studentAndGrade[0][1]
for index in range(1,len(studentAndGrade)):
    if studentAndGrade[index][1] == lowestScore:
        pass
    else:
        secondLowestScorePosition = index
        break

#  Checking to see if the secondLowestScore position is the last position
#  in the list. If it is the rest of the script doesn't need to run.
if secondLowestScorePosition == len(studentAndGrade)-1:
    #  Printing the student and grade and exiting.
    print studentAndGrade[secondLowestScorePosition][0]
    exit(1)

#  Creating list that will hold the second to lowest scores.
secondToLowestScoreList = []

#  Another for loop to find all scores that match the second to lowest
#  score
for index in range(secondLowestScorePosition,len(studentAndGrade)):

    if studentAndGrade[index][1] == studentAndGrade[index+1][1]:
        #  Adding the entry to the secondToLowestScoreList
        # secondToLowestScoreList.append(studentAndGrade[index])
        secondToLowestScoreList.insert(0,studentAndGrade[index])

        #  Checking to see if current index is one away from end of list.
        #  This will deal with situations like the following:
        #  [['Test1',52],['Test2',53],['Test3',53]]
        if index == len(studentAndGrade)-2:
            #  Adding last value in list to secondToLowestScoreList
            secondToLowestScoreList.append(studentAndGrade[index+1])
            #  Printing the list of names
            printListOfNames(secondToLowestScoreList)
            #  Exiting
            exit(1)
    else:
        #  Appending the final duplicate (second lowest score) to the list
        #  or appending only one score to the list.
        # secondToLowestScoreList.append(studentAndGrade[index])
        secondToLowestScoreList.insert(0,studentAndGrade[index])
        break


#  Printing list of second to lowest scores.
printListOfNames(secondToLowestScoreList)
