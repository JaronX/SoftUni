number = input()
number = reversed(number)

for i in number:
   num = int(i)
   if num == 0:
       print("ZERO")
   else:
       num += 33
       print(chr(num) * (num - 33))