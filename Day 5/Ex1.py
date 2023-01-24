# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height = 0
for height in student_heights:
    total_height += height 
print(f"Total height is: {total_height}")

num_students = 0
for student in student_heights:
    num_students += student
print(f"Total number of students are: {num_students}")

avg_height = round(total_height/num_students,0)
print(f"The average height is: {avg_height}")
