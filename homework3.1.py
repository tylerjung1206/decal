#1

def powerfunc(x,y):
    answer = 1
    for i in range(y):
        answer *= x
    return answer

x=2
y=5

print(powerfunc(x,y))

#2

my_list = [4,6,16,2]

def minmax(my_list):

    z = my_list[0]
    w = my_list[0]

    for i in my_list:
        if i < z:
            z = i
        elif i > w:
            w = i


    return z, w


print(minmax(my_list))


#3

year = 2024

def leapyeartest(ph):
    return (ph % 4 == 0) and (ph % 100 != 0 or ph % 400 == 0)

print(leapyeartest(year))

#4

weight = 110
height = 72
def bmi(weight,height):
    return 703*(weight/(height**2))

print(bmi(weight,height))

#5

n = 56789

def rotate_digits(n):
    s = n % 10
    j = n // 10
    nod = -1
    while n != 0:
        n //= 10
        nod += 1
    k = s * (10 ** nod) + j
    return k

k = rotate_digits(n)

print(k)