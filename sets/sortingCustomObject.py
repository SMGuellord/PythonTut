from operator import itemgetter

users = [
    {'fname': 'Bucky', 'lname': 'Roberts'},
    {'fname': 'Tom', 'lname': 'Roberts'},
    {'fname': 'Bernie', 'lname': 'Zuncks'},
    {'fname': 'Jenna', 'lname': 'Hayes'},
    {'fname': 'Amanda', 'lname': 'Williams'},
    {'fname': 'Bernie', 'lname': 'Barbie'},
    {'fname': 'Tom', 'lname': 'Williams'},
    {'fname': 'Dean', 'lname': 'Hayes'},
    {'fname': 'Tom', 'lname': 'Barbies'},
    {'fname': 'Sally', 'lname': 'Jones'},
]


for x in sorted(users, key=itemgetter('fname')):
    print(x)

print('-----------------')
for x in sorted(users, key=itemgetter('fname', 'lname')):
    print(x)