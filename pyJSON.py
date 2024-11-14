#

import json


#
data1 = {

'name':'Andrei',
'age':28,
'city':'Seattle, WA',
'interests':['Traveling', 'Hiking', 'Sailing', 'Surfing', 'Videogames', 'History', 'Camping', 'Nature photography'],
'is_student': True

}



with open('data1.json','w') as json_file:

    json.dump(data1,json_file,indent=4) 


    print('U have successfully written to data1.json')



with open ('data1.json', 'r') as json_file:
    loaded_data1 = json.load(json_file)


print('Successfully able to print data.json')
print(loaded_data1) 

loaded_data1['age'] = 21
loaded_data1['interests'].append('Muay Thai')


with open('data1.json','w') as json_file:

    json.dump(loaded_data1,json_file,indent=4) 


    print('U have successfully re-written to data1.json')




























