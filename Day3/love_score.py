# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = name1 + name2
full_name = name.lower()

t = full_name.count("t")
r = full_name.count("r")
u = full_name.count("u")
e = full_name.count("e")

true = t + r + u + e

l = full_name.count("l")
o = full_name.count("o")
v = full_name.count("v")
e = full_name.count("e")

love = l + o + v + e
love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score < 50) and (love_score > 40):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"your score is {love_score}")

