
print("================================= ")
print("for loop")
print("=================================")
foods = ['bacon', 'tuna', 'ham', 'sausages', 'beef']

#for loop
#for f in foods:
for f in foods[:2]:# loops to the index 2
    print(f)
    print(len(f))

print("================================= ")
print("Range")
print("=================================")
#range
for x in range(10, 20):
    print(x)

print("=================================")
print("While loop")
print("==================================")
#while loop

number = 5
while number < 10:
    print(number)
    number +=1