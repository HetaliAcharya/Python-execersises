# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# Don't change the code above 

# code below
import random
indx = []
for i in range(len(names)):
  indx.append(i)
#print(indx)
for i in range(len(indx)):
  name = random.randint(0,(len(indx)-1))
print(names[name])

