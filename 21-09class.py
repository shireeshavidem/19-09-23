#List[]
#slicing of a list[:]

#Add elements to a list
# 1. append() adds an item at the end of the list
# list = ['p','y','t','h','o','n']
# list2 =['p','r','o','g','r','a','m']
# list.append(list2)
# print(list)

#2.extend()to add all the items of an 
# iterable(list,tuple,string,etc)to end of list
list = ['p','y','t','h','o','n']
list2 =['p','r','o','g','r','a','m']
# list.extend(list2)
# print(list)

#insert()
list.insert(1,"ok")
print(list)

#change list items
list[2] = "me"
print(list)

#remove an item from a list
#Using del statement
del list2[3]
print(list2)

#using remove()
list2.remove('r')
print(list2)

#pop() function returns and removes item present at the given index
list.pop(1)
print(list)

#clear() removes all items from the list
#aliasing it changes only identity not values
a = [1,2,3,4,5,6,7]
b = a[:]
print(b)
print(id(a))
print(id(b))

#cloning is also changes the identity not values
#but also returns the shallow copy of the list
x = [23,43,56,43,21,7]
y = x.copy()
print(y)
print(id(x))
print(id(y))

#index()
animals = ["cat","dog","pig","dog"]
b = animals.index("dog",2)
print(b)

#sort() by giving this function defaultly 
# arrange the elements in assending order
x.sort()
print(x)

#reverse()
x.reverse()
print(x)
#for loop 
for animal in animals:
    print(animal)

#using in keyword
print("dog" in animals)

#list comprehension
numbers = [n**2 for n in range(1,8)]
print(numbers)
