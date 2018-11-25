#argument with a default value.
def get_gender(sex='unknown'):
    if sex is 'm':
        sex = "Male"
    elif sex is 'f':
        sex = "Female"
    print(sex)


def dumb_sentence(name='Bucky', action='ate', item='tuna'):
    print(name, action, item)


print("==========================================")
print("Function with default argument value")
print("============================================")
get_gender('m')
get_gender('f')
get_gender()

print("==========================================")
print("Function with keyword argument value")
print("============================================")
dumb_sentence("Sally", "eat", "slowly")
dumb_sentence(item="banana")
dumb_sentence(name="Sally", action="cooks")

