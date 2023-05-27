# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print(names)

total_person = len(names)
print(total_person)
#pick_person = random.randint(0 , Total_person -1)
#person_who_will_pay = names[pick_person]
#print(person_who_will_pay + "is going to buy a meal today!")
