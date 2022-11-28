# escolhido will

# A = ["mateus","samoel","geovane","marcelo","gean","katiana","iago"]
# B = ["diego","will","adriano","lucas","caio","guilherme","maria"]
# C = ["taynã","rafael","luan","douglas","alexandre","joão","camila"]

# A1 = []
# B1 = []
# C1 = []
# coloque a lista onde contem o escolhido sempre no meio 


    


# if(A){
#     B + A + C
# }else if(B){
#     A + B + C
# }else{
#     A + C + B
# }


# A + B + C

# A = ["mateus","marcelo","iago","adriano","guilherme","rafael","alexandre"]
# B = ["samoel","gean","diego","lucas","maria","luan","joão"]
# C = ["geovane","katiana","will","caio","taynã","douglas","camila"]

# A + C + B

# A = ["mateus","adriano","alexandre","will","douglas","gean","maria"]
# B = ["marcelo","guilherme","geovane","caio","camila","diego","luan"]
# C = ["iago","rafael","katiana","taynã","samoel","lucas","joão"]

# B + A + C

# conte de 0 a 10 ou de 1 a 11 e la esta o escolhido

# resultado = ["marcelo","guilherme","geovane","caio","camila","diego","luan","mateus","adriano",
#         "alexandre","will","douglas","gean","maria","iago","rafael","katiana","taynã","samoel","lucas","joão"]

# D = B + A + C
# print(D)
# for i in range(7):

#     A1.append(D[i])
#     i+3
#     B1.append(D[i])
#     i+3
#     C1.append(D[i])
#     i+3
#     print(A1)
    



# print(A[i],B[i],C[i])
# for i in range(7):
#     B.append

# for i in range(7):
#     C.append







# lista = []
# lista1 = []
# for i in range(3):
#     lista.append(i)

# for i in range(4):
#     lista1.append(i)
    
# lista3 = lista + lista1










# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# a = ["mateus","samoel","geovane","marcelo","gean","katiana","iago"]
# b = ["diego","will","adriano","lucas","caio","guilherme","maria"]
# c = ["taynã","rafael","luan","douglas","alexandre","joão","camila"]
a = ["a1","a2","a3","a4","a5","a6","a7"]
b = ["b1","b2","b3","b4","b5","b6","b7"]
c = ["c1","c2","c3","c4","c5","c6","c7"]
print('a      b      c')

for i in range(7):
    print(a[i]+ '    '+b[i]+'    '+c[i])
comando = input('digite a coluna onde esta o escolhido:   ')
if comando == "a":
    li = b + a + c

if comando == "b":
    li = a + b + c

if comando == "c":
    li = b + c + a

a = []
b = []
c = []

y = 0
for i in range(7):  # 0 a 6
     
    a.append(li[y])
    b.append(li[y+1])
    c.append(li[y+2])
    y  += 3

print(a)
print(b)
print(c)

print('a      b      c')

for i in range(7):
    print(a[i]+ '     '+b[i]+'      '+c[i])

comando = input('digite a coluna:   ')

if comando == "a":
    li = b + a + c

if comando == "b":
    li = a + b + c

if comando == "c":
    li = b + c + a


a = []
b = []
c = []

y2 = 0
for i in range(7):  # 0 a 6
     
    a.append(li[y2])
    b.append(li[y2+1])
    c.append(li[y2+2])
    y2  += 3

print(a)
print(b)
print(c)

print('a      b      c')
for i in range(7):
    print(a[i]+ '     '+b[i]+'      '+c[i])

comando = input('digite a coluna:   ')

if comando == "a":
    li = b + a + c

if comando == "b":
    li = a + b + c

if comando == "c":
    li = b + c + a


a = []
b = []
c = []
y3 = 0
for i in range(7):  # 0 a 6
     
    a.append(li[y3])
    b.append(li[y3+1])
    c.append(li[y3+2])
    y3  += 3


print("o numero escolhido é : "+li[10])





