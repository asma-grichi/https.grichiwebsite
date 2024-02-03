from numpy import array
def saisir():
    global n
    n=int(input("donner n"))
    while not (n>0):
        n=int(input("donner n"))
def remplir():
    for i in range(n):
        for j in range(n):
            m[i,j]=int(input("["+str(i)+","+str(j)+"]"))
def affichage():
    for i in range(n):
        for j in range(n):
            print(m[i,j],end=" ")
        print()
##pp
saisir()
m=array([[int()]*n]*n)
remplir()
affichage()
            