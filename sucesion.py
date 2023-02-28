n= int(input("Numero de 'n's a las que elevar el 10: "))

print("Aqui el comando de latex:")

print(R"\begin{equation} \frac{1}{10^1} ",end=" ")



for x in range(2,n+1):
    print(R"+ \frac{1}{10^"+str(x)+R"} ",end="")

print (R"\end{equation}")

print("El numero resultante es:")

total = 0
for x in range(1,n+1):
    total += 1/(10**x)

print(total)