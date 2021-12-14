#1
# list1 = [100, 200, 300, 400, 500]
# list1.reverse()
# print(list1)

#2
# list1 = ["M", "na", "i", "Mi"]
# list2 = ["y", "me", "s", "Ke"]
# list3 = []
# for i in range (len(list1)) :
#     list3.append( list1[i] + list2[i])
# print(list3)


#3
# numbers = [0, 1, 2, 3, 4, 5, 6, 7]
# numbers1 = []
# for i in range(len(numbers)):
#     numbers1.append(i * i)

# print(numbers1)

#4
# list1 = ["Goodbye ", "take "]
# list2 = ["Madame", "Sir"]
# list3 = []
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         list3.append(list1[i] + list2[j])

# print(list3)

#5
# list1 = [20, 30, 40, 50]
# list2 = [100, 200, 300, 400]
# list2.reverse()
# list3 = []
# for i in range(len(list1)):
#     list3.append(str(list1[i]) + " " +str(list2[i]))
#     print(list3[i])

#6
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
listLength = len(list1)

for i in list1:
    if list1[i].value == "":
        list1.remove(i)
    
print(list1)