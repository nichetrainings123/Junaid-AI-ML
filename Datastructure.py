"""
Data Structure in puython 
1.List :
    - List is a collection which is ordered and changeable. Allows duplicate members.
    - List items are indexed, the first item has index [0], the second item has index [1] etc.
    - Lists are written with square brackets.
    syntax : list_name = [item1, item2, item3]
2.Tuple :
    - Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    - Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
    - Tuples are written with round brackets.
    syntax : tuple_name = (item1, item2, item3)
3.Set :
    - Set is a collection which is unordered and unindexed. No duplicate members.
    - Sets are written with curly brackets.
    syntax : set_name = {item1, item2, item3}
4.Dictionary :
    - Dictionary is a collection which is ordered and changeable. No duplicate members.
    - Dictionary items are indexed, the first item has index [0], the second item has index [1] etc.
    - Dictionaries are written with curly brackets, and they have keys and values.
    syntax : dict_name = {key1: value1, key2: value2, key3: value3}
"""
##List
fruits = ["apple", "banana", "cherry"]
#Accessing List Items
print(fruits[0]) # Output: apple
print(fruits[1]) # Output: banana
print(fruits[2]) # Output: cherry
#Adding List Items
fruits.append("orange")
print(fruits) # Output: ['apple', 'banana', 'cherry', 'orange']
#Inserting List Items
fruits.insert(1, "kiwi")
print(fruits) # Output: ['apple', 'kiwi', 'banana', 'cherry', 'orange']
#Removing List Items
fruits.remove("banana")
print(fruits) # Output: ['apple', 'kiwi', 'cherry', 'orange']
#Sorting List Items
fruits.sort()
print(fruits) # Output: ['apple', 'cherry', 'kiwi', 'orange']
#Displaying List Items
print(fruits) # Output: ['apple', 'cherry', 'kiwi', 'orange']
#Reversing List Items
fruits.reverse()
print(fruits) # Output: ['orange', 'kiwi', 'cherry', 'apple']

####Tuple
Student = ("John", "Doe", 25)
print(Student) # Output: ('John', 'Doe', 25)
#Counting Tuple Items
print(Student.count("John")) # Output: 1
#Indexing Tuple Items
print(Student.index("Doe")) # Output: 1

###Set
number = {10, 20, 30, 40, 50}
print(number)
##Adding Set Items
number.add(60)
##Removing Set Items
number.remove(20)
#Update
number.update([70, 80, 90])
print(number) # Output: {10, 30, 40, 50, 60, 70, 80, 90}
print(number) # Output: {10, 30, 40, 50, 60, 70, 80, 90}

##Dictionary
student = {"name": "John", "age": 25, "city": "New York"}
print(student) # Output: {'name': 'John', 'age': 25, 'city': 'New York'}
#Accessing Dictionary Items
print(student["name"]) # Output: John
print(student["age"]) # Output: 25
print(student["city"]) # Output: New York
#Adding Dictionary Items
student["grade"] = "A"
print(student) # Output: {'name': 'John', 'age': 25, 'city': 'New York', 'grade': 'A'}
#Removing Dictionary Items
del student["age"]
print(student) # Output: {'name': 'John', 'city': 'New York', 'grade': 'A'}
#Add new key-value pair
student.update({"country": "USA"})
print(student) # Output: {'name': 'John', 'city': 'New York', 'grade': 'A', 'country': 'USA'}
#Update the Value
student["grade"] = "A+"
print(student) # Output: {'name': 'John', 'city': 'New York', 'grade': 'A+', 'country': 'USA'}
#Remove the Key-Value Pair
student.pop("city")
print(student) # Output: {'name': 'John', 'grade': 'A+', 'country': 'USA'}
#Display the Dictionary
print(student) # Output: {'name': 'John', 'grade': 'A+', 'country': 'USA'}
print(student)