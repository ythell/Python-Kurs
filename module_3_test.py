print('----==== 1 ====---')
lst = [1, 2,3, 4]
#      |  | |  |
#    [-4,-3-2,-1]
print(lst[-3:-2])

print('----==== 2 ====---')
var = 0
while var < 6:  # 0 < 6,     1 < 6
    var += 1    # 0 = 0 +1,  1 = 1 + 1
    if var % 2 == 0:    # 1 % 2 == 0 == False,   2 % 2 == 0 == True
        continue    # skip,  execute
    print("#")      # execute,   skip

print('----==== 3 ====---')
lista_1 = [1,2,3]
for v in range(len(lista_1)):   #petla v = 0,   v=1
    lista_1.insert(1,lista_1[v]) #lisya_1.insert(1,lista_1[0] -> lista_1.insert(1,1), lisya_1.insert(1,lista_1[1] -> lista_1.insert(1,1)
print(lista_1) #lista_1 = [1,1,2,3], lista_1 = [1,1,1,2,3]

print('----==== 4 ====---')
var = 1
while var < 10: # 1 < 10,   2 < 10, 4 < 10, 8 < 10, 16 < 10 = False
    print("#")  # print #,  print #, print #, print #
    var = var << 1 # var = 1*2 = 1, var = 2 * 2 = 4, var = 4 * 2 = 8, var = 8  * 2 = 16

print('----==== 5 ====---')
print([i for i in range(-1,2)]) # i for i in 3 -> [-1],[0],[1]

print('----==== 6 ====---')
vals = [0,1,2]
vals.insert(0,1) # [1,0,1,2]
del vals[1] # [1,1,2]
print(vals)

print('----==== 7 ====---')
i = 0
while i <= 5:   # 0 <= 5,, 1 <= 5
    i += 1  # 0 = 0 + 1, 1 = 1 + 1
    if i % 2 == 0: #False, True
        break   #         , execute
    print("*")  # print #

print('----==== 8 ====---')
z = 10
y = 0
print(y < z and z > y or y > z and z < y) # True and True or False and False = True

print('----==== 9 ====---')
a = 1
b = 0
print(a & b, a | b, a ^ b) # a and b = 0, a or b = 1, a XOR b = 1

print('----==== 10 ====---')
print(True == True) # True

print('----==== 11 ====---')
t = [[3-i for i in range(3)] for j in range(3)] # t = [[3, 2, 1], [3, 2, 1], [3, 2, 1]]
s = 0
for i in range(3):
    s += t[i][i] # s = 0 + [3], s = 3 + [2], s = 5 + [1]
print(s) # 6

print('----==== 12 ====---')
print(1 == 1) # True

print('----==== 13 ====---')
for i in range(1): # for i in 0
    print("#")  # print #
else:           # execute
    print("#")  # print #

print('----==== 14 ====---')
lst = [[0,1,2,3] for i in range(2)] # lst = [[0,1,2,3], [0,1,2,3]]
# print(lst[2][0])    # out of range

print('----==== 15 ====---')
i = 0
while i <= 3: # 0 <=3,  2 <= 3, 4 <= 3 False
    i +=2   # i = 0 + 2, i = 2 + 2
    print("*")  # print *, print *

print('----==== 16 ====---')
lst  = [3,1,-2]
print(lst[lst[-1]]) # lst[lst[-1]] = lst[-2] -> print 1

print('----==== 17 ====---')
vals = [0,1,2,]
vals[0], vals[2] = vals[2], vals[0] # first right gets assigned to first left and second right get assigned to second left at the same time

print('----==== 18 ====---')
nums = [1,2,3]
vals = nums # vals -> nums = [1,2,3]
del vals[1:2] # vals = [1, 3] & nums = [1, 3]
print(vals, nums)

print('----==== 19 ====---')
lista1 = [1,2,3]
lista2 = []        #lista2 = [1], lista2 = [2,1], lista2=[3,2,1]
for v in lista1: # v = 1, v = 2, v = 3
    lista2.insert(0,v) # lista2 = [1], lista2 = [2,1], lista2=[3,2,1]
print(lista2)

print('----==== 20 ====---')
nums = [1,2,3]
vals = nums[-1:-2] # [start:stop:step] from left to right, never opposite
print(vals, nums)