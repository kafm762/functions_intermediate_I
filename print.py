
x = [ [5,2,3], [10,8,9] ]
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ]

x = [ [5,2,3], [10,8,9] ]
x [1][0] = 15 

# Change the last_name of the first student from 'Jordan' to 'Bryant'

students[0]['last_name'] = "Bryant"
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = "Andres"
print (sports_directory)

# Change the value 20 in z to 30

z[0]['y'] = 30
print(z)


# Iterate through a list of dictionaries 
names = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(list):
    for i in range(0, len(list)):
        output=""
        for key,val in list[i].items():
            output = key + " - " + val
            print(output)
    
iterateDictionary(names)
        
        
# Get Values From a List of Dictionaries
names = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterate_dictionary2(key_name,list):
    for i in range(0, len(list)):
        for key,val in list[i].items():
            if key == key_name:
                print(val)
iterate_dictionary2('first_name',names)

def iterate_dictionary2(key_name,list):
    for i in range(0, len(list)):
        for key,val in list[i].items():
            if key == key_name:
                print(val)

iterate_dictionary2('last_name',names)

#Iterate Through a Dictionary with List Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    for key,val in dict.items():
        print("--------------")
        print len(val),key.upper()
        for i in range(0, len(val)):
            print(val[i])

printInfo(dojo)


    











