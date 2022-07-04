# 🚨 preq code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#code below this line 👇

name1 = name1.lower()
name2 = name2.lower()

#T count
name1_t = name1.count("t")
name2_t = name2.count("t")
t = name1_t+name2_t

#R count
name1_r = name1.count("r")
name2_r = name2.count("r")
r = name1_r+name2_r
#U count
name1_u = name1.count("u")
name2_u = name2.count("u")
u = name1_u+name2_u
#E count
name1_e = name1.count("e")
name2_e = name2.count("e")
e = name1_e+name2_e
#True total
t1 = t+r+u+e


#L count
name1_l = name1.count("l")
name2_l = name2.count("l")
l = name1_l+name2_l
#O count
name1_o = name1.count("o")
name2_o = name2.count("o")
o = name1_o+name2_o
#V count
name1_v = name1.count("v")
name2_v = name2.count("v")
v = name1_v+name2_v

#Love total
t2 = l+o+v+e

Total = int(str(t1)+str(t2))
if (Total > 90) or (Total < 10):
  print(f'Your score is {Total}, you go together like coke and mentos.')
elif((Total >= 40) and (Total <= 50 )):
  print(f'Your score is {Total}, you are alright together.')
else:
  print(f'Your score is {Total}.')
