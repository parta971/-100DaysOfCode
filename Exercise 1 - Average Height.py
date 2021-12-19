
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

student_heights_len=0

for l in student_heights:
    student_heights_len+=1

total_height=0

for i in student_heights:
    total_height+=i

avg_height=round(total_height/student_heights_len)
print(avg_height)


