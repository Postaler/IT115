#Import JSON module to work with JSON

import json


# Create a dictionary with key-value pairs
data1 = {

'name':'Andrei',
'age':28,
'city':'Seattle, WA',
'interests':['Traveling', 'Hiking', 'Sailing', 'Surfing', 'Videogames', 'History', 'Camping', 'Nature photography'],
'is_student': True

}


# Using "with" statement with 'open' function to open data1 in write mode. Assign the file object returned to the variable json_file.
with open('data1.json','w') as json_file:

    json.dump(data1,json_file,indent=4)   #dump converts our dictionary into JSON format, writes our data to file "json_file", keeps 4 indents.


    print('U have successfully written to data1.json')
# Prints a message


with open ('data1.json', 'r') as json_file:     ## Opens the file data1.json in read mode. Assign the file object returned to the variable json_file. This variable is used to reference the file within the with block.
    loaded_data1 = json.load(json_file) # Reads the JSON data from the file object json_file. Converts the JSON data back into a Python dictionary. The contents of data1.json are now stored in the variable loaded_data1.


print('Successfully able to print data1.json')
print(loaded_data1) #Prints info stored in loaded_data1

loaded_data1['age'] = 21 #Loaded_data1 holds dictionary info from our json file. We access key-value pair by using key "age" and replace its value to 21.
loaded_data1['interests'].append('Muay Thai') #we access interests list and append "Muay Thai" to it.


with open('data1.json','w') as json_file: #Opens the data1.json file in write mode to overwrite it. 

    json.dump(loaded_data1,json_file,indent=4) #Writes the updated loaded_data1 dictionary back to the data1.json file in JSON format.


    print('U have successfully re-written to data1.json')




























