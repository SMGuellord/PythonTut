from operator import attrgetter


class User:

    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    def __repr__(self):  # string representation of the object. equivalent of toString()
        return self.name + " : " + str(self.user_id)


users = [
    User('Bucky', 43),
    User('Sally', 5),
    User('Tuna', 61),
    User('Brian', 2),
    User('Joby', 77),
    User('Amanda', 9)
]

for user in users:
    print(user)


print('---------Sort by name-------------')
for user in sorted(users, key=attrgetter('name')):
    print(user)

print('---------Sort by id-------------')
for user in sorted(users, key=attrgetter('user_id')):
    print(user)