
import numpy as np

# 1

arr = np.array([[1,1,1],
                [1,2,3],
                [2,2,2]])

def findeq(arr):
    arreq = np.all(arr == arr[:,:1], axis=1)
    return arr[arreq]

print(findeq(arr))


#2

def chbd():
    cb = np.zeros((8,8))

    cb[::2, ::2] = 1
    cb[1::2, 1::2] = 1
    return cb

print(chbd())

#3

myarr = np.array(['python', 'is', 'cool!'])

space = np.char.join(" ", myarr)

print(space)

#4

np.random.seed(12345)
a = np.random.randint(1,50, (4, 5))
print(a)

def sort(a):
    sortarr = np.sort(a, axis = 0)
    return sortarr

print(sort(a))
