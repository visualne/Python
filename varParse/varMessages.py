import re


class messageCounter:
    def __init__(self):
        #  Checking each value in the list
        self.f = open('messages', 'r+')

        #  This variable keeps track of all the programs that were seen.
        self.programsList = []

        #  This variable keeps track of the program and # of times
        #  it was seen.
        self.programDict = {}

        #  This variable keeps track of the date seen and the total
        #  number of times certain programs were seen during that date.
        self.timeProgramDict = {}


    def countEntries(self):
        for line in self.f.readlines():

            #  Regex to look for date and program name
            match = re.match(r'(\w+\s\d+\s\d+\:\d+)\:\d+\s\w+\s([\w\-]+)',
                             line)

            #  Pulling date and program name
            date = match.group(1)
            program_name = match.group(2)


            #  Checking to see if date is a key in the timeProgramDict.
            if date in self.timeProgramDict.keys():

                #  Checking to see if the program_name is already in the
                #  program dictionary.
                if program_name in self.programDict.keys():
                    self.programDict[program_name] = self.programDict[program_name] + 1
                else:
                    self.programDict[program_name] = 1

                # Adding the program and number of times the program was seen
                #  for that time to the dictionary.
                if program_name in self.timeProgramDict[date].keys():
                    self.timeProgramDict[date][program_name] = \
                        self.programDict[program_name]
                else:
                    #  Changing timeProgramDict appropriately.
                    self.timeProgramDict[date] = self.programDict


                # Checking to see if the program exists in all of the
                #  programs that were found thus far.
                self.programs_list = self.checkProgramList(self.programDict, \
                                                      self.programsList)

            # This else path deals with situations where time does not exist
            #  in timeProgramDict. A BRAND NEW ASSOCIATED WILL TAKE PLACE IN
            #  IN THIS CASE
            else:

                #  Clear existing programDict
                self.programDict = {}

                #  New program found for the first time.
                self.programDict[program_name] = 1

                #  This deals with a situation where a brand new date is found
                #  and a brand new program.
                self.timeProgramDict[date] = self.programDict

                # Checking to see if the program exists in all of the
                #  programs that were found thus far.
                self.programs_list = self.checkProgramList(self.programDict, \
                                                      self.programsList)

        # Closing file handler.
        self.f.close()

    def printFinalOutput(self):
        #  Printing final output in the following format
        #  DATE TOTAL PROGRAM1 PROGRAM2 PROGRAM3 PROGRAM4.....
        print 'DATE TOTAL ' + ','.join(self.programsList)

        #  Creating temporary list that will hold the counts
        #  associated with each program.
        programsSeenCount = []

        #  Looping through timeProgramDict
        for timestamp in self.timeProgramDict.keys():
            #  Check the values against the program_list.
            for program in self.programsList:
                if program in self.timeProgramDict[timestamp].keys():
                    programsSeenCount.append(
                        str(self.timeProgramDict[timestamp][program]))
                else:
                    programsSeenCount.append('0')

            # Printing out the counts associated withe timestamps.
            print timestamp + ' ' + str(
                sum(self.timeProgramDict[timestamp].values())) + ' ' \
                  + ','.join(programsSeenCount)

            #  Clearing programsSeenCount to start over.
            programsSeenCount = []


    def checkProgramList(self,programDict,programsList):

        #  Checking to see if program is in the programs list.
        for program in self.programDict.keys():
            if program in self.programsList:
                pass
            else:
                return self.programsList.append(program)

        #  Returning unaltered programList
        return self.programsList



#  Creating messageCounter object
messageCounterObj = messageCounter()
messageCounterObj.countEntries()
messageCounterObj.printFinalOutput()
