print("==========================================")
print("writing to file...")

#Creating and Writing to file
fw = open('sample.txt', 'w')
fw.write('Writing some stuff in my text file \n')
fw.write('I like bacon\n')
fw.close()

print("==========================================")
print("Reading file...")
print("===========================================")
#Reading from a file
fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()