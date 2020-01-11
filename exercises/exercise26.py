import os
#  Write something that hits an api endpoint and recursively prints
#  all employees that fall underneath that employee
employeeId = 1


# def getEmployeeList(employeeId,count=0)
#
#     #  Calling the api
#     r = requests.get('http://someapithatreturnemployees/'+employeeId)
#
#     count = count + 1
#     for employee in r.response:
#         #  Call the function again
#         print count*'-'+employee
#         getEmployee(employee,count)
#
#     else:
#         pass


#  Original call
# getEmployeeList(employeeId)

def listFilesInDirectory(dir,count=0):
    count = count + 1
    for file in os.listdir(dir):
        #  If file is directory do recursive call.
        if os.path.isdir(file):
            path = os.getcwd()+'/'+ file
            print count*'-' + path
            listFilesInDirectory(path,count)
        else:
            path = dir+'/'+ file
            print count*'-' + path


#  To church up above
def getEmployees(id,count=0):
    count = count + 1

    r = requests.get('path_to_some_api/'+ employeeID)

    if len(r.reponse > 0):
        for employee in r.response:
            print count*'-'+employee

            #  Recursive function call.
            getEmployee(employee,count)
    else:
        print count*'-'+employee




listFilesInDirectory(os.getcwd())