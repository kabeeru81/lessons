'''
people = [
            {"name": "Kabir", "age":12, 
             "school":{"name":"Alqalam", "state":"Katsina"}, 
             "hobbies":["chess", "music"]
            },
            {"name": "Jamil", "age":15, 
             "school":{"name":"Bayero", "state":"Kano"}, 
             "hobbies":["programming", "drinking tea"]
            },
              {"name": "Usman", "age":19, 
             "school":{"name":"Dutse", "state":"Jigawa"}, 
             "hobbies":["working", "getting stressed"]
            },
              {"name": "Mohd", "age":16, 
             "school":{"name":"Alqalam", "state":"Katsina"}, 
             "hobbies":["snapchat", "music"]
            },
                {"name": "Kasandrah", "age":13, 
             "school":{"name":"FUT", "state":"Minna"}, 
             "hobbies":["anime", "learning"]
            },
]

<<<<<<< HEAD
# q1: """ For each person in the list of people, print out a sentence stating their names, age, where they school and what they like doing """
# q2: """ Create a variable that returns a sum of all the ages in the people list """
# q3: """"Create a variable that returns a list of all school names """
# q4: """ Create a variable that returns a list of all the first hobbies of each person"""


print('Kassandrah')


names = people[0]['name'],people[1]['name'],people[2]['name'],people[3]['name'],people[4]['name']

ages =people[0]['age'],people[1]['age'],people[2]['age'],people[3]['age'],people[4]['age']

school =people[0]['school']['name'],people[1]['school']['name'],people[2]['school']['name'],people[3]['school']['name'],people[4]['school']['name']

location = people[0]['school']['state'],people[1]['school']['state'],people[2]['school']['state'],people[3]['school']['state'],people[4]['school']['state']

hobbies =people[0]['hobbies'],people[1]['hobbies'],people[2]['hobbies'],people[3]['hobbies'],people[4]['hobbies']

age=people[0]['age']+people[1]['age']+people[2]['age']+people[3]['age']+people[4]['age']

hobby =people[0]['hobbies'][-2],people[1]['hobbies'][-2],people[2]['hobbies'][-2],people[3]['hobbies'][-2],people[4]['hobbies'][-2]

# for person in names:
print(f'{names[0]} is {ages[0]} years old from {school[0]} in {location[0]}, and loves {hobbies[0][-2]} and {hobbies[0][-1]}')
print(f'{names[1]} is {ages[1]} years old from {school[1]} in {location[1]}, and loves {hobbies[1][-2]} and {hobbies[1][-1]}')
print(f'{names[2]} is {ages[2]} years old from {school[2]} in {location[2]}, and loves {hobbies[2][-2]} and {hobbies[2][-1]}')
print(f'{names[3]} is {ages[3]} years old from {school[3]} in {location[3]}, and loves {hobbies[3][-2]} and {hobbies[3][-1]}')
print(f'{names[4]} is {ages[4]} years old from {school[4]} in {location[4]}, and loves {hobbies[4][-2]} and {hobbies[4][-1]}')

print(f'the schools are : {school}')
print (f'the ages sum up to {age}')
print(f'the first hobbies of each person are: {hobby}')
=======
q1: """ For each person in the list of people, print out a sentence stating their names, age, where they school and what they like doing """
q2: """ Create a variable that returns a sum of all the ages in the people list """
q3: """" Create a variable that returns a list of all school names """
q4: """ Create a variable that returns a list of all the first hobbies of each person"""
'''
>>>>>>> 979e0c6cc1c71c80e77af3ae58db71401e0c573f

Kabir Abubakar
>>> names = people[0]['name'], people[1]['name'],people[2]['name'],people[3]['name'],people[4]['name']
>>> names
('kabir', 'jamil', 'usman', 'Mohd', 'Kasandrah')
>>> ages=people[0]['age'],people[1]['age'],people[2]['age'],people[3]['age'],people[4]['age']
>>> ages
(12, 15, 19, 16, 13)
>>> schools = people[0]['school']['name'],people[1]['school']['name'],people[2]['school']['name'],people[3]['school']['name'],people[4]['school']['name']
>>> schools
('AlQalam', 'bayero', 'Dutse', 'Alqalam', 'FUT')
>>> states = people[0]['school']['state'],people[1]['school']['state'],people[2]['school']['state'],people[3]['school']['state'],people[4]['school']['state']
>>> states
('katsina', 'kano', 'Jigawa', 'Katsina', 'Minna')
>>> hobbies = people[0]['hobbies'][0],people[1]['hobbies'][0],people[2]['hobbies'][0],people[3]['hobbies'][0],people[4]['hobbies'][0]
>>> hobbies
('chess', 'programming', 'working', 'snapchat', 'anime')
>>> hobbies2 = people[0]['hobbies'][1],people[1]['hobbies'][1],people[2]['hobbies'][1],people[3]['hobbies'][1],people[4]['hobbies'][1]
>>> hobbies2
('music', 'drinking tea', 'getting stressed', 'music', 'learning')


""" Create a variable that returns a sum of all the ages in the people list """
>>> sum_ages = sum(ages)
>>> sum_ages
75
>>>
>>> sums = people[0]['age']+people[1]['age']+people[2]['age']+people[3]['age']+people[4]['age']
>>> sums
75


>>>
>>> '" Create a variable that returns a list of all school names '
>>> schools = people[0]['school']['name'],people[1]['school']['name'],people[2]['school']['name'],people[3]['school']['name'],people[4]['school']['name']
>>>schools
('AlQalam', 'bayero', 'Dutse', 'Alqalam', 'FUT')


     """ Create a variable that returns a list of all the first hobbies of each person"""
>>> hobbies = people[0]['hobbies'][0],people[1]['hobbies'][0],people[2]['hobbies'][0],people[3]['hobbies'][0],people[4]['hobbies'][0]
>>> hobbies
('chess', 'programming', 'working', 'snapchat', 'anime')



