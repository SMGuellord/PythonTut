class Girl:

    gender = 'female'

    def __init__(self, name):
        self.name = name


r = Girl('Rachel')
s = Girl('Stanky')

print(r.name)
print(r.gender)
print(s.name)
print(s.gender)