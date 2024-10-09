target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
sum=0
for even in range(2,int(target+1),2):
  sum+=even
print(f'even sumation:{sum}')

alt_sum=0
for odd in range(1,int(target+1)):
 if odd % 2 != 0:
  alt_sum+=odd
print(f'odd sumation:{alt_sum}')