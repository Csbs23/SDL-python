
print("----capitalize----")
mystatement = "welcome to hubspot"
myvalue = mystatement.capitalize()
print(myvalue)


print("----append----")
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")


print("----clear----")
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()


print("----copy----")
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()


print("----split----")
statement = "python is fun and easy"
myvalue = statement.split()
print(myvalue)

print("----extend----")
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)

print("----strip----")
mystatement = '     Removes all the unnecessary spaces  '
print(mystatement.strip())


print("----upper----")
mystatement = 'welcome to hubspot'
print(mystatement.upper())


print("----sort----")
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()


print("----lower----")
x = 'WELCOME TO HUBSPOT'
print(x.lower())


print("----find----")
my_str = "Python is a powerful language"
index_result = my_str.find("language")
print(index_result)


print("----casefold----")
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)


print("----center----")
txt = "banana"
x = txt.center(20)
print(x)


print("----count----")
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)


print("----encode----")
txt = "My name is Ståle"
x = txt.encode()
print(x)


print("----endswith----")
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)


print("----index----")
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)


print("----issalnum----")
txt = "Company12"
x = txt.isalnum()
print(x)


print("----isalpha----")
txt = "CompanyX"
x = txt.isalpha()
print(x)


print("----isdecimal----")
txt = "1234"
x = txt.isdecimal()
print(x)


print("----isascii----")
txt = "Company123"
x = txt.isascii()
print(x)


print("----replace----")
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

print("----partition----")
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)



  