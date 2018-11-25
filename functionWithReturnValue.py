#What age of a woman is a man allowed to date?
def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return girls_age

#using the function.

buckys_limit = allowed_dating_age(30)
print("Bucky can date date girls", buckys_limit,"or older")