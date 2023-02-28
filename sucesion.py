n= int(input("Numero de 'n's a las que elevar el 10: "))

print("Aqui el comando de latex:")

print(R"\begin{equation} \frac{1}{10^1} ",end=" ")

expresion ="0.1 "

for x in range(2,n+1):
    print(R"+ \frac{1}{10^"+str(x)+R"} ",end="")
    expresion = expresion + "+ " + str(1/(10**x)) + " "

print (R"\end{equation}")

total = 0
for x in range(1,n+1):
    total += 1/(10**x)

print("Expresion: ")

print(expresion)

print("El numero resultante es:")

print(total)
