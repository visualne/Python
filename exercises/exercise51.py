# Complete the arrayManipulation function below.
def arrayManipulation(queries,max_value_array_dictionary):

    #  Pulling the current maximum value out of the dictionary
    current_max_value = max_value_array_dictionary.keys()[0]

    #  Pulling the current array out of dictionary
    current_array = max_value_array_dictionary[current_max_value]

    #  For loop to parse each input value
    for start_end_index_and_value in queries:
        input_values = start_end_index_and_value.split(' ')
        start_index = int(input_values[0]) - 1
        end_index = int(input_values[1])
        value_added = int(input_values[2])


        #  For loop to perform operation on existing array
        for index in range(start_index,end_index):
            current_array[index] = current_array[index] + value_added

            #  if statement to check the current_max_value against
            #  the current element being worked on in the array.
            if current_array[index] > current_max_value:
                current_max_value = current_array[index]

    print(current_max_value)
    return current_max_value


#  Opening input file
input_file = open('input','r')

all_inputs = input_file.readlines()

array_size_and_num_elements = all_inputs[0].split(' ')

#  Getting array size
array_size = array_size_and_num_elements[0]

#  Getting number of elements
num_elements = array_size_and_num_elements[1]

#  Getting sample_inputs
sample_inputs = all_inputs[1:]

#  Creating an array that is of size specified.
array = [0] * int(array_size)

#  Creating dictionary that will hold the current
#  max value as a key and the value for that key
#  will be what the current list looks like after
#  operations are performed on it.
#  example) {200: [100,100,200,0]} <-200 is the max value of the current list
max_value_array_dictionary = {
    0:array
}

max_value = arrayManipulation(sample_inputs,
                              max_value_array_dictionary)

print(max_value)