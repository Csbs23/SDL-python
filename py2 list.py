# Adds List Element as value of List. 
List = ['Mathematics', 'chemistry', 1997, 2000] 
List.append(20544) 
print(List) 

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 
print(List.count(1)) 

List = ['Mathematics', 'chemistry', 1997, 2000] 
# Insert at index 2 value 10087 
List.insert(2, 10087) 
print(List) 

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 
print(List.index(2)) 

List1 = [1, 2, 3] 
List2 = [2, 3, 4, 5] 
  
# Add List2 to List1 
List1.extend(List2) 
print(List1) 
  
# Add List1 to List2 now 
List2.extend(List1) 
print(List2) 

List = [1, 2, 3, 4, 5] 
print(sum(List)) 

numbers = [5, 2, 8, 1, 9] 
print(min(numbers)) 

numbers = [5, 2, 8, 1, 9] 
print(max(numbers))

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 
print(List.pop())

numbers = [21, 34, 54, 12]
numbers.append(32)
print(numbers)

languages = ['Python', 'Swift', 'C++']
print("Total Elements: ", len(languages)) 