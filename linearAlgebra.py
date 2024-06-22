import numpy as np
'''
#split, join 연습
split = "I love python!".split()
print(split)
join = ' '.join(split)
print(join)

#list comprehension
newlist = [i + j for i in split for j in join]
print(newlist)
newnewlist = [[i + j for i in split] for j in join]
print(newnewlist)


#zip 연습
num1 = [1, 10, 100]
num2 = [2, 20, 200]
num3 = [i for i in zip(num1, num2)]
print(num3)

#람다 연습
f = lambda x : x ** 2
print(f(9))
print((lambda x, y : x**2 +2*x*y + y**2)(2, 3))
'''

x = [2, 2]
y = [2, 3]
z = [3, 5]
vectorSum = [sum(i) for i in zip(x, y, z)]
print(vectorSum)
scalaProduct = [2 * sum(i) for i in zip(x, y, z)]
print(scalaProduct)

matrixA = [[1, 2], [3, 4]]
matrixB = [[5, 6], [7, 8]]
matrixSum = [[sum(i) for i in zip(matrixA, matrixB)]]