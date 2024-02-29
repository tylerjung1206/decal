 #2.1 

tyler = [] # I initially tried to do [range(51)], but it would just print "range(51)", so I had to createa loop so each individual number would be printed
for i in range(51):
    tyler.append(i)

#2.2
    
def sq(tyler):
    tylersq = [] #I was just getting the same numbers, so I realized I needed to create a new list, and append the squared number into that list
    for i in tyler:
        tylersq.append(i ** 2)
    
    return tylersq


print(sq(tyler))

#2.3

list1 = []
for j in range(11):
    list1.append(j)

list2 = []
for k in range(20,31):
    list2.append(k)


def listodd(list1,list2):
    oddlist = []
    for n in list1:
        if n % 2 != 0:        # at first I tried oddlist.append(2n+1) without an if statement, but this caused extra numbers past 9/29 to be inputted
            oddlist.append(n) # I fixed it by the use of modulus and != to identify odd numbers
    for m in list2:
        if m % 2 != 0:
            oddlist.append(m)

    return oddlist
    

print(listodd(list1,list2))


#3.1

list = []

count = 1
for z in range(5): #I initially used the z and l as the counter for the values in the list, but I realized I couldn't add the values past 5 when it loops to next rows, so I used a separate counter that added each time the loop went around
    row = []
    for l in range(5):
        row.append(count)
        count += 1
    list.append(row) 


for row in list: #I just printed list at first, but this just put all the lists in order, so I had to use the for loop so it would print on separate lines
    print(row,",")

#3.2

for i in range(5):
    for j in range(5):  # I first tried to "row" directly into the for statement, but that didn't work, so I used an arbitrary counter that was then impelmented in "list[][]" to identify the specific elements in the rows that needed to be swapped
        if list[i][j] % 3 == 0:
            list[i][j] = "?"

for row in list:
    print(row,",")

#4 

llist = [1,1,1,1,1,2,3,3,4,5,5,6,6,7,8]
llist2 = []  # I first didn't establish a new list and tried to remove from the originial, but thats too complicated. With the new list, I could use "not in" to easily remove duplicates

def listremove(llist):
    for x in llist:
        if x not in llist2:
            llist2.append(x)
    return llist2 # I forgot to return the new list at first; simple mistake
   


print(listremove(llist))