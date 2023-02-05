# Restar 2 numeros n1 y n2. Implementar un algoritmo que sin usar el - se sumen
# def resta(n1,n2):
#     resultado=n1
#     for i in range(n2):
#         resultado-=1
#     print(resultado)

#resta(7,2)

def div(n1,n2):
    resul=0
    while n1>=n2:
        n1-=n2
        resul+=1
    print(resul)

div(10,2)

# def multi(n1,n2):
#     resul=0
#     while n2>0:
#         n2-=1
#         resul+=n1
#     print(resul)    

# multi(5,3)
