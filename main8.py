#lambda, filter, map, zip, enumerate, list comprehension

#list comprehension
# a = [i if i%2==0 else 0 for i in range(1,10)]
# print(a)

#enumerate
# a = [0, 2, 0, 4, 0, 6, 0, 8, 0]
# for indx,val in enumerate(a):
# print(indx,val)

#zip
# a = (1,2,4,5,6)
# b = "abcd"
# f = {45:"b",54:"c",87:"fr"}
# for i in zip(a,b,f.values()):
# print(i)

#lambda

# def summa(x,y):
# return x+y

# summa = lambda x,y: x+y if x%2==0 else 0
#
# print(summa(8,6))

#map
# def pow(x):
# if x%2==0:
# return 1
# else:
# return x
# a = [1,2,3,4,5,6]
# a = list(map(pow, a))
# print(a)

#filter
# a = [1, 2, 3, 4, 5, 6]
# a = list(filter(lambda x: x % 2, a))
# print(a)


#сортировка по ключу

# a = [(1,0,5),(3,0,4),(-5,-1,3),(5,-2,2)]
# maxx = max(a,key=lambda x:x[2])
# print(maxx)

