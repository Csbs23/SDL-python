print("--if--")
a = 15
if a > 10:
   print("a is greater")

print("--if else--")
a = 15
b = 20
if a > b:
   print("a is greater")
else:
   print("b is greater")

print("--Nested if Statements--")
num = 15
if num >= 0: 
    if num == 0: 
        print("Zero") 
    else: 
        print("Positive number") 
else: 
    print("Negative number") 

print("--elif ladder statements--")
a = 15
b = 15
if a > b:
   print("a is greater")
elif a == b:
   print("both are equal")
else:
   print("b is greater")

print("--while--")
   i = 1
while i < 6:
  print(i)
  i += 1

  print("--break--")
  i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1