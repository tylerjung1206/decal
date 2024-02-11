#6

list = [123,14,8,36,70]

def minfor(list):
    
    minfor = list[0]

    for i in list:
        if i < minfor:
            minfor = i

    return minfor

print(minfor(list))


def minwhile(list):
    
    minwhile = list[0]
    j = 0

    while j < len(list):

        if list[j] < minwhile:
            minwhile = list[j]
        j += 1

    return minwhile

print(minwhile(list))


def maxfor(list):
    
    maxfor = list[0]

    for i in list:
        if i > maxfor:
            maxfor = i

    return maxfor

print(maxfor(list))

def maxwhile(list):
    
    maxwhile = list[0]
    j = 0

    while j < len(list):

        if list[j] > maxwhile:
            maxwhile = list[j]
        j += 1

    return maxwhile

print(maxwhile(list))

#7

word = "headphones"

def numbvowel(word):
    vowelcount = 0
    vowels = {'a','e','i','o','u','A','E','I','O','U'}
    for char in word:
        if char in vowels:
            vowelcount += 1

    return vowelcount

print(numbvowel(word))

#8

number = 12345

def sum(number):
    
    ognumber = number
    nod = 0
    while number != 0:
        number //= 10
        nod += 1

    number = ognumber
    b = 0
    while nod != 0:
        a = number % 10
        b += a
        number //= 10
        nod -= 1

    return b

print(sum(number))


