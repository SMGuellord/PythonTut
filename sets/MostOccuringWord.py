from collections import Counter


text = "Education, best described as the process of imparting or receiving knowledge, is one of the highest priorities on the global agenda. Across the world, governments and organised groups are working to eradicate illiteracy in order to emancipate impoverished people groups. Education can take place in formal and informal settings, however, schools and learning institutions are the primary mediums through which people receive an education in modern society. Reading and writing are the foundations of formal education."

words = text.split()

counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)