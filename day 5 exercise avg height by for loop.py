# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇

total_height=0
for height in student_heights:
  total_height += height
print(f'total height:{total_height}')

total_length=0
for length in student_heights:
  total_length += 1
print(f'number of student:{total_length}')

avg_height=total_height/total_length

print(f'average height:{avg_height}')