#  1. Create a list of 5 integers and display the list items. Access individual elements through index.
ls=[1,2,3,4,5]
for i in range(0,len(ls)):
    print(ls[i])


#  2. Append a new item to the end of the list.
ls.append(6)
print(ls)

#  3. Reverse the order of the items in the list.
ls.reverse()
print(ls)

# 4. Print the number of occurrences of a specified element in a list.
alphabets=['a','a','b','v','b','g']
print(alphabets.count('a'))

#  5. Append the items of list1 to list2 in the front.
ls1=[1,2,3]
ls2=[4,5,6]
ls2=ls1+ls2
print(ls2)

# 6. Insert a new item before the second element in an existing list.
ls.insert(1,234)
print(ls)

# 7. Remove the item from a specified index in a list.
ls.pop(1)
print(ls)

# 8. Remove the first occurrence of a specified element from a list.
list=[1,2,1,3,1,4]
list.remove(1)
print(list)