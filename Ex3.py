# **********add to each element its index**************************
lst = [0, 1, 2, 3, 4]
lst1 = []
i = 0
while i < 5:
    N = input("enter a number: ")
    lst1.append(N)
    i += 1

lst2 = list(zip(lst, lst1))
print(lst2)


# **************find the all unique elements**************************
i = 0
unique_lst = []

while i < 5:
    lst = input("enter a number: ")
    for j in lst:
        if j not in unique_lst:
            unique_lst.append(j)
    i += 1
print(unique_lst)

# •	Input another list. find all elements from first list that not included in second one
i = 0
j = 0
x = 0
lst1 = []
lst2 = []
element = []
TT = []
while int(x) <= 3:
    FList = input("enter a number for first list: ")
    lst1.append(FList)
    SList = input("enter a number for second list: ")
    lst2.append(SList)
    x += 1
    for i in lst1:
        if i not in lst2:
            element.append(i)
            # helps to remove the first index in case ut shows in lst2
        elif lst1[0] in element:
            TT = lst1[0]
            element.remove(lst1[0])

print("first list: ", lst1)
print("second list: ", lst2)
print("element: ", element)
print("TT: ", TT)
