# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum = 0
for height in student_heights:
    sum += height

total_number = 0
for student in student_heights:
    total_number += 1



average_height = round(sum / total_number)
print(average_height)
