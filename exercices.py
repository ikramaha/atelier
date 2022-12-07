#exercice: calcule de puissance:
def puissance (n,p):
    x=1
    for i in range (p):
        x*=n
    return (x)
print(puissance(4,3))

# exercice: calcul de somme 
def somme (p):
    for i in range (p):
        p+=i
    return p 
print (somme(7))        


#exercice: factorielle 
def factorielle(X):
    fact=1
    for i in range (1,X+1):
        fact*=i
    return fact 
print(factorielle(8))        


#exercice: suite factorielle(i)/i
def factorielle(X):
    fact=1
    for i in range (1,X+1):
        fact*=i
    return fact
def sum(n):  
    a=0
    for i in range(1,n+1):
        a+=factorielle(i)/1
    return a
print(sum(6))           


#EXERCICE: len number:
def number(x):
    return(len(str(x)))
print(200)    